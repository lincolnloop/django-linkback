#!/usr/bin/env python
from setuptools import setup, find_packages

VERSION = __import__('linkback').__version__

setup(
    name="django-linkback",
    version=VERSION,
    author='Lincoln Loop: Nicolas Lara',
    author_email='info@lincolnloop.com',
    description=("An admin widget to show a link back to the original objects in foreign keys."),
    packages=find_packages(),
    package_data={'linkback': [
        'static/linkback/js/*.js',
        'static/linkback/img/*.gif',
        'templates/linkback/*.html',
        'templates/linkback/admin/*.html',
        'templates/linkback/admin/widgets/*.html'
    ]},
    url="http://github.com/lincolnloop/django-linkback/",
    install_requires=['setuptools'],
    classifiers=[
        'Development Status :: 0.1 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
