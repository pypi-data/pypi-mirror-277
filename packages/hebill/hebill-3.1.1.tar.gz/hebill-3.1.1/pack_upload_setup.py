# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
setup(
    name='hebill',
    version='3.1.1',
    description='Hebill Python Library',
    long_description=open(r'README.MD', encoding='utf-8').read(),
    long_description_content_type='text/plain',
    packages=find_packages(include=[
        'hebill',
        'hebill.*',
    ]),
    package_data={
        'hebill': ['*.md', '*.MD'],
    },
    install_requires=[
        'colorama==0.4.6',
        'numpy==1.26.4',
        'wxPython==4.2.1',
        'pillow==10.3.0',
    ],
    python_requires='>=3.12',
)
