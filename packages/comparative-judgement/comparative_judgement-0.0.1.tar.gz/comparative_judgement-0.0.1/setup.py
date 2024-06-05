from setuptools import setup, find_packages

setup(
    name = 'comparative_judgement',
    version = '0.0.1',
    packages = find_packages(),
    install_requires = [
        'numpy',
        'scipy',
        'matplotlib',
    ],
    author = 'Andy Gray',
    description = 'A package for conducting Comparative Judgement',
    long_description = open('README.md').read(),
    long_description_content_type = 'text/markdown',
)