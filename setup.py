from setuptools import setup, find_packages

setup(
    name='simple-pip-example',
    version='0.0.1',
    author="Your name here",
    author_email="your@email.com",
    packages=find_packages(),
    # packages=find_packages(
    #     where='src',
    #     include=["simple*"],
    #     exclude=['additional'],
    # ),
    # package_dir={"": "src"},
    install_requires=[
        # dependencies here
    ],
)