from __future__ import annotations

from typing import Any, Tuple

from airflow.hooks.base import BaseHook
import configparser

class IbmpaHook(BaseHook):
    """
    Ibmpa Hook that interacts with an HTTP endpoint the Python requests library.

    :param method: the API method to be called
    :type method: str
    :param sample_conn_id: connection that has the base API url i.e https://www.google.com/
        and optional authentication credentials. Default headers can also be specified in
        the Extra field in json format.
    :type sample_conn_id: str
    :param auth_type: The auth type for the service
    :type auth_type: AuthBase of python requests lib
    """

    conn_name_attr = "ibmpa_conn_id"
    default_conn_name = "ibmpa_default"
    conn_type = "ibmpa"
    hook_name = "IBM Planning Analytics"

    @staticmethod
    def get_ui_field_behaviour() -> dict:
        """Returns custom field behaviour"""
        return {
            "hidden_fields": ["Extra"],
            "relabeling": {},
            "placeholders": {
                "host": "PA Server IP Address",
                "port": "PA Server HTTP Port",
            },
        }

    def __init__(
        self,
        ibmpa_conn_id: str = default_conn_name,
    ) -> None:
        super().__init__()
        self.ibmpa_conn_id = ibmpa_conn_id

    def get_conn(self) -> configparser.ConfigParser:
        """
        Returns http session to use with requests.

        :param headers: additional headers to be passed through as a dictionary
        :type headers: dict
        """
        conn = self.get_connection(self.ibmpa_conn_id)
        self.ibmpa_config = configparser.ConfigParser()
        self.ibmpa_config[self.ibmpa_conn_id] = {}
        self.ibmpa_config[self.ibmpa_conn_id]['address'] = conn.host
        self.ibmpa_config[self.ibmpa_conn_id]['port'] = str(conn.port)
        self.ibmpa_config[self.ibmpa_conn_id]['user'] = conn.login
        self.ibmpa_config[self.ibmpa_conn_id]['password'] = conn.password
        self.ibmpa_config[self.ibmpa_conn_id]['ssl'] = 'True' if conn.schema == 'https' else 'False'

        return self.ibmpa_config