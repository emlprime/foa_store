import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, find_packages

import os

setup(
    name = 'satchmo-livesettings',
    version = '0.1.4',
    description = "Satchmo Livesettings",
    long_description = """It is a spin-off project from Satchmo (configure settings via an admin interface).""",
    #author = 'Oleg Dolya',
    url = 'http://bitbucket.org/jbo/satchmo-livesettings/',
    license = 'BSD',
    platforms = ['any'],
    #install_requires=["django-keyedcache"],
    classifiers = ['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],    
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
)
