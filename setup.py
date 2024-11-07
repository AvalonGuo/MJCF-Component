from setuptools import setup, find_packages

setup(
    name='mjcomponent',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'mujoco',
        'dm-control',
    ],
)