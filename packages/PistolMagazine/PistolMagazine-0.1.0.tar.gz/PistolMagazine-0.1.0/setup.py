from setuptools import setup, find_packages

setup(
    name='PistolMagazine',
    version='0.1.0',
    description='A data mocking tool designed to help you generate realistic data for testing and development purposes.',
    author='Ealyn',
    author_email='miyuk1@126.com',
    packages=find_packages(),
    install_requires=[
        'Faker==25.1.0'
    ],
)
