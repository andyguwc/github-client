# -*- coding: utf-8 -*-
import click
from cmd.repo import repo


@click.group()
@click.option(
    '-a',
    '--api-token',
    help='your API key for the Github API',
)
@click.pass_context
def cli(ctx, api_token):
    ctx.obj = {
        'api_token': api_token,
    }


cli.add_command(repo)


if __name__ == '__main__':
    cli()
