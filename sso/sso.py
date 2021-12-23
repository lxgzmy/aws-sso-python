import boto3
import click


@click.group()
@click.option('--profile', default=None,
              help="Use a given AWS profile.")
def cli(profile):
    """sso fetch tempory tokens from AWS."""
    global session

    session_cfg = {}
    if profile:
        session_cfg['profile_name'] = profile

    session = boto3.Session(**session_cfg)


@cli.command('list-buckets')
def list_buckets():
    """List all s3 buckets."""
    print("test")


if __name__ == '__main__':
    cli()
