from setuptools import setup

setup(
    name='sso',
    version='0.1',
    author='Jason Lau',
    author_email='lxgzmy@gmail.com',
    description='using python package to fetch token from aws sso automaticaly.',
    license='GPLv3+',
    packages=['sso'],
    url='https://github.com/lxgzmy/aws-sso-python',
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        sso=sso.sso:cli
    '''
)
