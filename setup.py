#
# Licensed under a 3-clause BSD style license - see LICENSE in top directory
#

from distutils.core import setup

setup(name='applausequery',
      version='0.0.1',
      description='Package to query APPLAUSE TAP service',
      author='Christian Dersch',
      author_email='christian.dersch@physik.uni-marburg.de',
      url='https://github.com/lupinix/applausequery',
      license='BSD',
      packages=['applausequery'],
      install_requires=[
          'astropy>=2.0',
          'pyvo>=0.9',
          'six',
      ]
     )
