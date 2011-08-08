# -*- coding: utf-8 -*-


from setuptools import find_packages
from setuptools import setup


setup(
    name='pythonkc-meetups',
    version='0.0.1',
    description='Provides PythonKC Meetup.com events.',
    license='MIT',
    url='https://github.com/estebistec/pythonkc-meetups',
    packages=find_packages(),
    install_requires=['distribute>=0.6.14', 'httplib2>=0.7.1', 
                      'mimeparse>=0.1.3', 'python-dateutil>=1.5,<2'],
    author='Steven Cummings',
    author_email='estebistec@gmail.com'
)
