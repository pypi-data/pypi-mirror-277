import logging

import curlify
from requests import Response, Session

from api_nichotined.core.response import ResponseHandler


class Api:
    def __init__(self, base_url, is_log_curlify=True):
        self.base_url = base_url
        self.session = Session()
        self.logger = logging.getLogger(__name__)
        self.is_log_curlify = is_log_curlify

    def close_session(self):
        if self.session:
            self.session.close()

    def _make_request(self, method, path, params=None, data=None, json_data=None, headers=None,
                      auth=None, files=None) -> ResponseHandler:
        url = self.base_url + path
        self.logger.info(f"Making {method} request to {url}")

        response = self.session.request(method, url, params=params, data=data, json=json_data, headers=headers,
                                        auth=auth, files=files)

        self.log_response(response)
        return ResponseHandler(response)

    def log_response(self, response: Response):
        if self.is_log_curlify:
            curl = curlify.to_curl(response.request)
            self.logger.info(curl)
            
        self.logger.info(f"Response received with status code {response.status_code}")
        self.logger.info(response.json())

    def get(self, path, params=None, data=None, json_data=None, headers=None, auth=None, files=None) -> ResponseHandler:
        return self._make_request("GET", path, params=params, data=data, headers=headers, json_data=json_data,
                                  auth=auth, files=files)

    def post(self, path, params=None, data=None, json_data=None, headers=None, auth=None,
             files=None) -> ResponseHandler:
        return self._make_request("POST", path, params=params, data=data, headers=headers, json_data=json_data,
                                  auth=auth, files=files)

    def put(self, path, params=None, data=None, json_data=None, headers=None, auth=None, files=None) -> ResponseHandler:
        return self._make_request("PUT", path, params=params, data=data, headers=headers, json_data=json_data,
                                  auth=auth, files=files)

    def delete(self, path, params=None, data=None, json_data=None, headers=None, auth=None,
               files=None) -> ResponseHandler:
        return self._make_request("DELETE", path, params=params, data=data, headers=headers, json_data=json_data,
                                  auth=auth, files=files)
