# -*- coding: utf-8 -*-


from setuptools import find_packages
from setuptools import setup


setup(
    name='pythonkc-meetups',
    version='0.0.5',
    description='Provides PythonKC Meetup.com events.',
    license='MIT',
    url='https://github.com/pythonkc/pythonkc-meetups',
    packages=find_packages(),
    install_requires=['distribute', 'requests>=0.7.5', 
                      'mimeparse>=0.1.3', 'python-dateutil>=1.5,<2'],
    author='Steven Cummings',
    author_email='estebistec@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries'
    ]
)
