from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE.md') as f:
    license = f.read()

setup(
    name='sepa',
    version='0.4.5',
    description='Python library for parsing and building SEPA Direct Debit and SEPA eMandate schemas.',
    long_description=readme,
    license=license,
    author='Vereniging Campus Kabel',
    author_email='info@vck.utwente.nl',
    url='https://github.com/VerenigingCampusKabel/python-sepa',
    packages=find_packages(exclude=('tests')),
    install_requires=['lxml >= 3.5.0, < 4', 'signxml'],
    test_suite='nose.collector',
    tests_require=['deep', 'xmltodict', 'nose'],
    package_data={
        'sepa': ['schemas/*.xsd']
    }
)
