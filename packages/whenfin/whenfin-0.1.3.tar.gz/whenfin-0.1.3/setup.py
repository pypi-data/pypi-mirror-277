from setuptools import setup, find_packages
setup(
  name='whenfin',
  version='0.1.3',
  author='Luca Dovichi',
  author_email='lucadovichi@uchicago.edu',
  description='Connects a Python program to Whenfin services',
  packages=find_packages(),
  classifiers=[
  'Programming Language :: Python :: 3',
  'Operating System :: OS Independent',
  ],
  python_requires='>=3.6',
)