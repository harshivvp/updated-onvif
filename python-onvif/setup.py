import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
version_path = os.path.join(here, 'onvif/version.txt')
version = open(version_path).read().strip()

requires = [ 'suds >= 0.4', 'suds-passworddigest' ]

CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Environment :: Console',
    'Intended Audience :: Customer Service',
    'Intended Audience :: Developers',
    'Intended Audience :: Education',
    'Intended Audience :: Science/Research',
    'Intended Audience :: Telecommunications Industry',
    'Natural Language :: English',
    'Operating System :: POSIX',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Multimedia :: Sound/Audio',
    'Topic :: Utilities',
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.6",
    "Programming Language :: Python :: 2.7",
]

wsdl_files = [ 'wsdl/' + item for item in os.listdir('wsdl') ]

setup(
      name='onvif',
      version=version,
      description='Python Client for ONVIF Camera',
      long_description=open('README.rst', 'r').read(),
      author='Cherish Chen',
      author_email='sinchb128@gmail.com',
      maintainer='sinchb',
      maintainer_email='sinchb128@gmail.com',
      license='MIT',
      keywords=['ONVIF', 'Camera', 'IPC'],
      url='http://github.com/quatanium/python-onvif',
      zip_safe=False,
      packages=find_packages(exclude=['docs', 'examples', 'tests']),
      install_requires=requires,
      include_package_data=True,
      data_files=[('wsdl', wsdl_files)],
      entry_points={
          'console_scripts': ['onvif-cli = onvif.cli:main']
          }
     )


