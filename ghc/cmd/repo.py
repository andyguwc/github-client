# -*- coding: utf-8 -*-
import click

import ghc.github as github


@click.group()
def repo():
    pass


@repo.command()
@click.option(
    '-n',
    '--number',
    required=False,
    default=10,
    type=int,
    help='Number of issues to view'
)
@click.pass_context
@github.command()
def ls(ctx, client, number):
    print(ctx.obj)
    # result = client.get_user_repos()
    # click.echo(result[:number])

