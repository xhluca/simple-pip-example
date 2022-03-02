from setuptools import setup, find_packages

setup(
    name='simple-pip-example',
    version='0.0.1',
    author="Your name here",
    author_email="your@email.com",
    url='https://yourwebsite.com',
    description='Your description here, e.g. from readme',
    packages=find_packages(
        where='src',
        include=["simple*"],
        exclude=['simple_hidden*'],
    ),
    package_dir={"": "src"},
    install_requires=[
        # dependencies here
    ],
    extras_require={
        # For special installation via pip install simple-pip-example[dev]
        'dev': 'black'
    }
)