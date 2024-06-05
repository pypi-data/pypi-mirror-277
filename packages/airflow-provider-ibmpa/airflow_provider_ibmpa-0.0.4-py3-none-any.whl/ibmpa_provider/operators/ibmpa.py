from __future__ import annotations

from typing import TYPE_CHECKING

from airflow.exceptions import AirflowException
from airflow.models import BaseOperator

from ibmpa_provider.hooks.ibmpa import IbmpaHook

if TYPE_CHECKING:
    from airflow.utils.context import Context


class IbmpaCubeViewToCsvOperator(BaseOperator):
    """
    Calls an endpoint on an HTTP system to execute an action.

    :param sample_conn_id: connection to run the operator with
    :type sample_conn_id: str
    :param endpoint: The relative part of the full url. (templated)
    :type endpoint: str
    :param method: The HTTP method to use, default = "POST"
    :type method: str
    :param data: The data to pass
    :type data: a dictionary of key/value string pairs
    :param headers: The HTTP headers to be added to the request
    :type headers: a dictionary of string key/value pairs
    """

    # Specify the arguments that are allowed to parse with jinja templating
    template_fields = [
        "cube",
        "view",
        "path",
        "file_name",
        "base_dt"
    ]

    def __init__(
        self,
        ibmpa_conn_id,
        cube,
        view,
        path,
        file_name,
        base_dt=None,
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.ibmpa_conn_id = ibmpa_conn_id
        self.cube = cube
        self.view = view
        self.path = path
        self.file_name = file_name
        self.base_dt = base_dt

    def execute(self, context: Context):
        from TM1py import TM1Service
        import os

        hook = IbmpaHook(ibmpa_conn_id=self.ibmpa_conn_id)
        config = hook.get_connection()

        with TM1Service(**config[self.ibmpa_conn_id]) as tm1:
            version = tm1.server.get_product_version()
            print(f'IBM PA Version: {version}')

            data = tm1.cubes.cells.execute_view_dataframe_pivot(self.cube, self.view)
            data.reset_index(inplace=True)

            if not os.path.exists(self.path):
                os.system(f'mkdir -p {self.path}')

            file_path = self.path + '/' + self.file_name
            print(file_path)
            data.to_csv(file_path, encoding='utf-8', index=False)