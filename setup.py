#!/usr/bin/env python3

from distutils.core import setup

setup(
    name='rgsim',
    version='1.0',
    description='Realm Grinder Simulator',
    author='James Bungard',
    author_email='jmbungard@gmail.com',
    url='https://www.github.com/repos/verdesmarald/rgsim',
    packages=['rgsim'],
    zip_safe=False,
    entry_points = {
        'console_scripts': ['rgsim=rgsim.gui.app:main'],
    }
)