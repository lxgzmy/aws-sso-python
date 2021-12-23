# aws-sso-python
using python package to fetch token from aws sso automaticaly.


#if want to run the source code in the sso folder, please use:
```python -m sso.sso```
#this way we treat the sso as package, so the reference in sso/sso.py path can be resloved.

#steps to build and deploy the packages for sso:
```pipenv uninstall setuptools```
#install the dependency, for lib like click and boto3
```pipenv install -d setuptools```

##Build
#generate the setup file and build the package to wheel package
```python3 setup.py bdist_wheel```

#this will build a wheel file in the dist folder, to install this wheel we can run:
```pip3 install dist/sso-0.1-py3-none-any.whl```

#To uninstall the package we can use
```pip3 uninstall sso```

#after we install the package, we can run:
```pip3 show sso```
#to see the package information.

#then after install the package we can run the sso direct like:

```sso --help```

#we can publish the wheel file to pypi, so public can use it, or upload to s3 or google drive, let someone else to download it, it can be installed and reused by anyone else.