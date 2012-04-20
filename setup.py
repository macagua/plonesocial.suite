from setuptools import setup, find_packages
import os

version = '0.1'

long_description = (
    open('README.txt').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='plonesocial.suite',
      version=version,
      description="Pre-integrated social business suite for Plone",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='plone socbiz social microblogging',
      author='Guido Stevens',
      author_email='guido.stevens@cosent.net',
      url='http://github.com/cosent/plonesocial.suite',
      license='gpl',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['plonesocial'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plonesocial.microblog',
          'plonesocial.activitystream',
          # -*- Extra requirements: -*-
      ],
      extras_require={'test': ['plone.app.testing']},
      entry_points="""
      # -*- Entry points: -*-
  	  [z3c.autoinclude.plugin]
  	  target = plone
      """,
      )