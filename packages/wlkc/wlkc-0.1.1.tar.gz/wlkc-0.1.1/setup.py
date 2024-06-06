#!/usr/bin/env python
# -*- coding:utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="wlkc",
    version="0.1.1",
    author="wlkc",
    author_email="wlkc@hotmail.com",
    description="A simple flask app for wlkc",
    long_description=open("README.md", "r", encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    # url="https://github.com/wlkc/ksjdf",
    packages=find_packages(),
    # package_dir={'ksjdf': 'ksjdf'},
    # package_data={
    #     'wlkc_core': ['views/*'],  # 包含 views 目录下的所有文件
    # },
    # exclude_package_data={'game': ["game/*"]},
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
    install_requires=[
        # 'flask==3.0.2',
        # 'flask-redis==0.4.0',
        # 'flask-sqlalchemy==3.1.1',
        # 'pymysql==1.1.1',

        # 'bcrypt==4.1.3',
        # 'Jinja2==3.1.3',
        # 'openpyxl==3.1.2',
        # 'cryptography==42.0.7',
        # 'pyjwt==2.8.0',
        # 'pillow==10.3.0',
        # 'cuid==0.4'
    ]
)
