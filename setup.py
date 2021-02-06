#!/usr/bin/python
# -*- coding=utf-8 -*-
from setuptools import setup

# to install type:
# python setup.py install --root=/
from io import open
def readme():
    with open('README.rst', encoding="utf8") as f:
        return f.read()

setup (name='Qamus', version='0.1',
      description="Qamus is an information retrieval tool that allows for documents indexing, similarity calculation, and search operations with both boolean and vector models.",
      long_description = readme(),      

      author='Ali Aouf',
      author_email='ali.aouf@gmail.com',
      url='https://40uf411.github.io/Qamus/',
      license='GPL',
      package_dir={'qamus': 'Qamus'},
      packages=['Qamus'],
      install_requires=[
      ],         
      include_package_data=True,
      package_data = {
        'Qamus': ['doc/*.*','doc/html/*', 'data/*.sqlite', 'data/*.sql'],
        },
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: End Users/Desktop',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          ],
    );