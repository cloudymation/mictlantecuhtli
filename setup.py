# _*_ coding: utf-8 _*_
# !/usr/bin/env python3

"""
Mictlantecuhtli: A Multi-Cloud Global Probe Mesh Creator.

@author: Collisio-Adolebitque
"""

import pathlib
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

dependencies = []
module_name = 'mictlantecuhtli'
short_description = 'This is a python module to provide a multi-cloud terraform command line tool'


setup(
    name=module_name,
    version='0.0.1',
    author='Collisio Adolebitque',
    author_email='collisio@net-devops.com',
    url='https://github.com/cloudymation/mictlantecuhtli',
    license='MIT',
    description=short_description,
    long_description=README,
    long_description_content_type='text/markdown',
    packages=['mictl'],
    package_data={},
    platforms='any',
    include_package_data=True,
    install_requires=dependencies,
    entry_points={
        "console_scripts": [
            "mictl=mictl.__main__:main"
        ]
    },
    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        # 'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
