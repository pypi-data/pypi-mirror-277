from setuptools import setup, find_packages

setup(
    name='hello_world_hemanth1',
    version='0.1',
    description='A simple Hello package for subtracting two numbers',
    author='Hemanthbollina123',
    author_email='hsbollina@gmail.com',
    packages=find_packages(),
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'subtract=hello_world.cli:main',
        ],
    },
)

