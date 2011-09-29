# Copyright (c) 2011 by Zocolab <pablo@zocolab.es>
#
# This software is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this software. If not, see <http://www.gnu.org/licenses/>.

import os
from setuptools import setup, find_packages


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(
    name="aretha",
    version="0.0.1",
    author="Pablo Recio Quijano",
    author_email="precio@zocolab.es",
    description="Django-based blogging system",
    long_description=(read('README')),
    classifiers=[
        'Development Status :: 1 - Planning',
        'Framework :: Django',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
    ],
    license="LGPL 3",
    keywords="django blog",
    url='https://github.com/Fsero/Aretha',
    packages=find_packages('.'),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Django>=1.3',
        'South',
        'psycopg2',
        'django-debug-toolbar',
        'django-transmeta',
        ],
)

# Dependencies:
# * Django               - Python-based web development framework
# * South                - Django application to simplify model SQL migrations
# * psycopg2             - To work with PostgreSQL
# * django-debug-toolbar - Add a debug toolbar on views with a lot of helper information
# * django-transmeta     - Allows to create translatable fields
