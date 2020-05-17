from setuptools import setup
 
setup(name='datatypes_validator',
      version='0.1',
      url='https://bitbucket.org/Cilium/datatype-validator/src/master/',
      license='GPL',
      author='Cilium',
      description='datatypes validator',
      packages=['datatype'],
      long_description=open('README.md').read(),
      zip_safe=False,
      install_requires=[
          'isbnlib', 'iso8601'
      ])