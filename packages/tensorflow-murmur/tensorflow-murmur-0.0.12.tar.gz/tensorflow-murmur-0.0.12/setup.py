from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='tensorflow-murmur',
  version='0.0.12',
  author='Ivan V. Savkin',
  author_email='i.v.savkin2020@yandex.ru',
  description='This is a small addons module for tensorflow',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://pypi.org/project/tensorflow-murmur/',
  packages=find_packages(),
  install_requires=['tensorflow','numpy','sklearn'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='tf addons',
  project_urls={
    'GitHub': 'https://github.com/jordmundgand/tensorflow_murmur'
  },
  python_requires='>=3.8'
)
