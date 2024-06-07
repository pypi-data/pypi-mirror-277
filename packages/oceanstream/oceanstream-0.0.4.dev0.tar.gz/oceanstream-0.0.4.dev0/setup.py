from os import path
from setuptools import find_packages, setup

current_filename = path.dirname(__file__)


def read_requirements(file_path):
    with open(file_path) as f:
        lines = f.read().splitlines()
    _requires = []
    _links = []
    for line in lines:
        if line.startswith("git+"):
            _links.append(line)
        else:
            _requires.append(line)
    return _requires, _links


def read_extra_requirements(module_name):
    file_path = path.join(current_filename, 'oceanstream', module_name, 'requirements.txt')
    if path.isfile(file_path):
        return read_extra_requirements(file_path)
    return []


install_requires, dependency_links = read_requirements(path.join(current_filename, 'requirements.txt'))

setup(
    name="oceanstream",
    version="0.1.3",
    description="OceanStream: process raw sonar data at scale",
    license="MIT",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Pineview Labs",
    author_email="hello@pineview.io",
    url="https://github.com/OceanStreamIO/oceanstream",
    packages=find_packages(include=['oceanstream', 'oceanstream.*']),
    python_requires=">=3.11",
    install_requires=install_requires,
    dependency_links=dependency_links,
    include_package_data=True,
    extras_require={
        'cli': read_extra_requirements('cli'),
        'echodata': read_extra_requirements('echodata'),
        'plot': read_extra_requirements('plot'),
        'denoise': read_extra_requirements('denoise'),
        'process': read_extra_requirements('process'),
        'exports': read_extra_requirements('exports'),
        'complete': [
            'cli',
            'echodata',
            'process',
            'denoise',
            'plot',
            'exports'
        ],
    },
    entry_points={
        'console_scripts': [
            'oceanstream=oceanstream.cli.main:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
