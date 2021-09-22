# -*- coding: utf-8 -*-
import functools

from .client import GithubClient

GITHUB_CLI_FIELDS = ['api_token']


def command():
    """Injects github client
    """
    def decorator(func):
        @functools.wraps(func)
        def func_wrapper(ctx, *args, **kwargs):
            """Pass an AWS client as the first argument in the command.
            """
            context = ctx.obj or {}
            client = GithubClient(api_token=context.get('api_token'))
            return func(ctx, client, *args, **kwargs)
        return func_wrapper
    return decorator
