from setuptools import setup
 
setup(name='datatypes_validator',
      version='0.3',
      url='https://bitbucket.org/Cilium/datatype-validator/src/master/',
      license='GPL',
      author='Cilium',
      description='datatypes validator',
      packages=['datatype', 'datatype.validators', 'datatype.xsd'],
      long_description=open('README.md').read(),
      zip_safe=False,
      install_requires=[
          'isbnlib', 'iso8601'
      ])