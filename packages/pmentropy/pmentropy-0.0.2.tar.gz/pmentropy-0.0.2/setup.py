from setuptools import setup, find_packages

try:
    import pypandoc
    long_description = pypandoc.convert_file('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

setup(
  name='pmentropy',
  version='0.0.2',
  author='Taverna Tanguy',
  author_email='taverna.tanguy@gmail.com',
  description='Compute in python entropy for process mining describe in Back, C.O., Debois, S. & Slaats, T. Entropy as a Measure of Log Variability. J Data Semant 8, 129–156 (2019). https://doi.org/10.1007/s13740-019-00105-3 (https://rdcu.be/dJMwH)',
  long_description=long_description,
  long_description_content_type='text/markdown',
  url= 'https://github.com/TavTanguy/pmentropy',
  packages=find_packages(),
  readme='README.md',
  license='GNU General Public License v3',
  license_file='LICENSE',
  install_requires=['numpy >= 1.26.4', 'pm4py >= 2.7.11.10', 'Levenshtein >= 0.25.1'],
  classifiers=[
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU Affero General Public License v3',
    'Programming Language :: Python :: 3.11',
  ])
