from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

# setup(
#     name='pdfmater',
#     version='0.1.0',
#     description='Package for reading pdfs and text into json and csvs',
#     long_description=readme,
#     author='Phillip Tinsley',
#     author_email='philliptinsley44@mgail.com',
#     url='https://github.com/kennethreitz/samplemod',
#     license=license,
#     packages=find_packages(exclude=('tests', 'docs'))
# ) ##

setup() ## this is because we're using toml file 