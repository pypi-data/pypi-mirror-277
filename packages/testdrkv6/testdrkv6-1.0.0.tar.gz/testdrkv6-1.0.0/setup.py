from setuptools import setup, find_packages

setup(
    name='testdrkv6',
    version='1.0.0',
    author="drkv - Duesseldorf - Germany",
    author_email="m.kirchhof@drkv.com",
    description="Python module to onboard the EC2 Utills Library",
    packages=find_packages(),
    install_requires=[
        "boto3 >= 1.28.10",
        "pycryptodome >= 3.20.0",
    ],
)