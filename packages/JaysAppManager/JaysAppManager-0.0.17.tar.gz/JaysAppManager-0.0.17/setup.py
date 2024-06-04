import os
from setuptools import setup, find_packages


build_num = os.getenv('CIRCLE_BUILD_NUM', '0')


VERSION = f'0.0.{build_num}'
DESCRIPTION = 'A helpful appmanager'
LONG_DESCRIPTION = 'A helpful appmanager'

setup(
    name="JaysAppManager",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author="Jay Fesco",
    author_email="jayfesco1@gmail.com",
    license='MIT',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'command = module.submodule:function',
            'register = register:register',
        ],
    },
)