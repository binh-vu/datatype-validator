from setuptools import setup
 
setup(name='datatypes-validator',
      version='0.1',
      url='https://bitbucket.org/Cilium/xsdvalidator/src/master/',
      license='GPL',
      author='Cilium',
      description='datatypes validator',
      packages=['datatypes'],
      long_description=open('README.md').read(),
      zip_safe=False,
      extras_require = {
            'build': ['isbnlib', 'iso8601']
      })