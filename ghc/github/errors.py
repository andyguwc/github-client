# -*- coding: utf-8 -*-


class GithubAPIError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"[Github API] {self.message}"
