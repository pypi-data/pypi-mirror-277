from setuptools import setup, find_packages

setup(
  name='pixegami_hhello',
  version='0.2',
  packages=find_packages(),
  description=('none'),
  install_requires=[],
  entry_points={
    'console_scripts': [
      'hello = pixegami_hhello.main:hello',
    ]
  }
)