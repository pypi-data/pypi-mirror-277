import time
from collections import OrderedDict

from biolib import api
from biolib._internal.http_client import HttpError
from biolib.biolib_errors import BioLibError, NotFound
from biolib.experiments.types import ExperimentDict
from biolib.jobs.job import Job
from biolib.jobs.types import JobsPaginatedResponse
from biolib.tables import BioLibTable
from biolib.typing_utils import Dict, List, Optional, Union


class Experiment:
    _BIOLIB_EXPERIMENTS: List['Experiment'] = []

    # Columns to print in table when showing Job
    _table_columns_to_row_map = OrderedDict(
        {
            'Name': {'key': 'name', 'params': {}},
            'Job Count': {'key': 'job_count', 'params': {}},
            'Created At': {'key': 'created_at', 'params': {}},
        }
    )

    def __init__(self, uri: str):
        self._experiment_dict: ExperimentDict = self._get_or_create_by_uri(uri)

    def __enter__(self):
        Experiment._BIOLIB_EXPERIMENTS.append(self)

    def __exit__(self, type, value, traceback):  # pylint: disable=redefined-builtin
        Experiment._BIOLIB_EXPERIMENTS.pop()

    def __str__(self):
        return f'Experiment: {self.name}'

    def __repr__(self):
        return f'Experiment: {self.name}'

    @property
    def uuid(self) -> str:
        return self._experiment_dict['uuid']

    @property
    def name(self) -> str:
        return self._experiment_dict['name']

    @staticmethod
    def get_experiment_in_context() -> Optional['Experiment']:
        if Experiment._BIOLIB_EXPERIMENTS:
            return Experiment._BIOLIB_EXPERIMENTS[-1]
        return None

    # Prints a table listing info about experiments accessible to the user
    @staticmethod
    def show_experiments(count: int = 25) -> None:
        experiment_dicts = api.client.get(path='/experiments/', params={'page_size': str(count)}).json()['results']
        BioLibTable(
            columns_to_row_map=Experiment._table_columns_to_row_map,
            rows=experiment_dicts,
            title='Experiments',
        ).print_table()

    def wait(self) -> None:
        self._refetch_experiment_dict()
        while self._experiment_dict['job_running_count'] > 0:
            print(f"Waiting for {self._experiment_dict['job_running_count']} jobs to finish", end='\r')
            time.sleep(5)
            self._refetch_experiment_dict()

        print(f'All jobs of experiment {self.name} have finished')

    def add_job(self, job_id: str) -> None:
        api.client.patch(path=f'/jobs/{job_id}/', data={'experiment_uuid': self.uuid})

    def mount_files(self, mount_path: str) -> None:
        try:
            # Only attempt to import FUSE dependencies when strictly necessary
            from biolib._internal.fuse_mount import (  # pylint: disable=import-outside-toplevel
                ExperimentFuseMount as _ExperimentFuseMount,
            )
        except ImportError as error:
            raise ImportError(
                'Failed to import FUSE mounting utils. Please ensure FUSE is installed on your system.'
            ) from error

        _ExperimentFuseMount.mount_experiment(experiment=self, mount_path=mount_path)

    def export_job_list(self, export_format='dicts'):
        valid_formats = ('dicts', 'dataframe')
        if export_format not in valid_formats:
            raise BioLibError(f'Format can only be one of {valid_formats}')

        job_dict_list = [job.to_dict() for job in self.get_jobs()]
        if export_format == 'dicts':
            return job_dict_list

        elif export_format == 'dataframe':
            try:
                import pandas as pd  # type: ignore  # pylint: disable=import-outside-toplevel
            except ImportError as error:
                raise ImportError(
                    'Pandas must be installed to use this method. '
                    'Alternatively, use .get_jobs() to get a list of job objects.'
                ) from error

            jobs_df = pd.DataFrame.from_dict(job_dict_list)
            jobs_df.started_at = pd.to_datetime(jobs_df.started_at)
            jobs_df.created_at = pd.to_datetime(jobs_df.created_at)
            jobs_df.finished_at = pd.to_datetime(jobs_df.finished_at)
            return jobs_df

    # Prints a table containing info about this experiment
    def show(self) -> None:
        BioLibTable(
            columns_to_row_map=Experiment._table_columns_to_row_map,
            rows=[self._experiment_dict],
            title=f'Experiment: {self.name}',
        ).print_table()

    # Prints a table listing info about the jobs in this experiment
    def show_jobs(self) -> None:
        response: JobsPaginatedResponse = api.client.get(
            path=f'/experiments/{self.uuid}/jobs/',
            params=dict(page_size=10),
        ).json()
        jobs: List[Job] = [Job(job_dict) for job_dict in response['results']]

        BioLibTable(
            columns_to_row_map=Job.table_columns_to_row_map,
            rows=[job._job_dict for job in jobs],  # pylint: disable=protected-access
            title=f'Jobs in experiment: "{self.name}"',
        ).print_table()

    def get_jobs(self, status: Optional[str] = None) -> List[Job]:
        job_states = ['in_progress', 'completed', 'failed', 'cancelled']
        if status is not None and status not in job_states:
            raise Exception('Invalid status filter')

        url = f'/experiments/{self.uuid}/jobs/'
        params: Dict[str, Union[str, int]] = dict(page_size=1_000)
        if status:
            params['status'] = status

        response: JobsPaginatedResponse = api.client.get(url, params=params).json()
        jobs: List[Job] = [Job(job_dict) for job_dict in response['results']]

        for page_number in range(2, response['page_count'] + 1):
            page_response: JobsPaginatedResponse = api.client.get(url, params=dict(**params, page=page_number)).json()
            jobs.extend([Job(job_dict) for job_dict in page_response['results']])

        return jobs

    def rename(self, name: Optional[str] = None, destination: Optional[str] = None) -> None:
        if destination:
            try:
                account_id = api.client.get(path=f'/account/{destination}/').json()['uuid']
            except HttpError as error:
                if error.code == 404:
                    raise NotFound(f'Destination "{destination}" not found.') from None
                else:
                    raise error

            api.client.patch(
                path=f'/apps/{self.uuid}/',
                data={'account_id': account_id},
                params={'resource_type': 'experiment'},
            )

        if name:
            api.client.patch(path=f'/apps/{self.uuid}/', data={'name': name}, params={'resource_type': 'experiment'})

        self._refetch_experiment_dict()

    @staticmethod
    def _get_or_create_by_uri(uri: str) -> ExperimentDict:
        experiment_dict: ExperimentDict = api.client.post(
            path='/experiments/',
            data={'uri' if '/' in uri else 'name': uri},
        ).json()
        return experiment_dict

    def _refetch_experiment_dict(self) -> None:
        self._experiment_dict = api.client.get(path=f'/experiments/{self.uuid}/').json()
