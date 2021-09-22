# -*- coding: utf-8 -*-
import requests
import os

import ghc.constants as constants
from ghc.github.auth import GithubAuth
from ghc.github.errors import GithubAPIError


class GithubClient(object):
    """
    Github http client
    """
    GITHUB_BASE_URL = "https://api.github.com"
    OWNER = "andyguwc"

    def __init__(
        self,
        session=None,
        api_token=None,
        base_url=GITHUB_BASE_URL,
    ):
        self.session = session or requests.Session()
        self.session.auth = GithubAuth(api_token=api_token or constants.GITHUB_API_TOKEN)
        self.session.headers.update({
            "Content-Type": "application/json",
        })
        self.base_url = base_url

    def request(self, endpoint, method='get', params=None, data=None, headers=None, **request_kwargs):
        url = os.path.join(self.base_url, endpoint)
        response = getattr(self.session, method)(
            url,
            params=params,
            data=data,
            headers=headers,
            **request_kwargs,
        )

        self._check_error(response)
        return response

    @staticmethod
    def _check_error(response):
        if 200 <= response.status_code < 300:
            return
        raise GithubAPIError(response.text)

    def get_user(self):
        return self.request('user')

    def get_user_repos(self):
        http_kwargs = {
            "endpoint": f"users/{self.OWNER}/repos",
        }
        return self.request(**http_kwargs).json()
