from setuptools import setup, find_packages

def readme():
  with open('readme.md', 'r', encoding='utf-8') as f:
    return f.read()

setup(
  name='365sms',
  version='1.1',
  author='Sterrist',
  author_email='griodred@gmail.com',
  description='Это библиотека для работы с API сервиса 365SMS',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/Herels2/365smsapi',
  packages=find_packages(),
  install_requires=['requests'],
  classifiers=[
    'Programming Language :: Python :: 3.12'
  ],
  keywords='365sms sms smsapi 365smsapi 365api',
  project_urls={
    'GitHub': 'https://github.com/Herels2'
  },
  python_requires='>=3.6'
)