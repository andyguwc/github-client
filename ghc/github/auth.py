# -*- coding: utf-8 -*-
import requests


class GithubAuth(requests.auth.AuthBase):
    """Github auth wrapper to populate token header
    """
    def __init__(self, api_token):
        self.api_token = api_token

    def __call__(self, request):
        request.headers.update({
            "Authorization": f"token {self.api_token}"
        })
        return request
