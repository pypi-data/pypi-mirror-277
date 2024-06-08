from setuptools import setup, find_packages

def readme():
  with open('readme.md', 'r', encoding='utf-8') as f:
    return f.read()

setup(
  name='keyapistr',
  version='1.0',
  author='Sterrist',
  author_email='griodred@gmail.com',
  description='NULLF',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/Herels2',
  packages=find_packages(),
  install_requires=['requests'],
  classifiers=[
    'Programming Language :: Python :: 3.12'
  ],
  keywords='nones',
  project_urls={
    'GitHub': 'https://github.com/Herels2'
  },
  python_requires='>=3.6'
)