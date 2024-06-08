import setuptools

with open('README.rst', 'r') as f:
  long_description = f.read()

setuptools.setup(
  name = 'markethours',
  version = '0.1.0',
  author = 'Mason Krause',
  description = 'A python library for referencing and localizing US stock trading hours',
  long_description = long_description,
  packages = setuptools.find_packages(),
  include_package_data = True,
  python_requires = '>=3.7',
  install_requires = [
    'requests',
    'pytz'])