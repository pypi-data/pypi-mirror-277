from distutils.core import setup
from setuptools import find_packages

with open('D:\zsodata\拾贝v1南网价格监控系统\zcbot-crawl-core\README.rst', 'r') as f:
    long_description = f.read()

setup(name='zcbot-crawl-core',
      version='2.0.25',
      description='zcbot crawl core for zsodata',
      long_description=long_description,
      author='zsodata',
      author_email='team@zso.io',
      url='http://www.zsodata.com',
      install_requires=['zcbot-url-parser'],
      python_requires='>=3.7',
      license='BSD License',
      packages=find_packages(),
      platforms=['all'],
      include_package_data=True
      )
