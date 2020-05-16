from setuptools import setup
 
setup(name='xsd-validator',
      version='0.1',
      url='https://bitbucket.org/Cilium/xsdvalidator/src/master/',
      license='GPL',
      author='Cilium',
      description='xsd validator',
      packages=['xsd_validator'],
      long_description=open('README.md').read(),
      zip_safe=False)