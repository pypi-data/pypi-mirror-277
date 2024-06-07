from setuptools import setup, find_packages

setup(
    name='logsnap',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'colorama'
    ],
    entry_points={
        'console_scripts': [
            'logsnap=logsnap.analyzer:main'
        ]
    },
    author='Ibrahim Hasnat',
    description='A simple log file analyzer with summary and search functionality.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    python_requires='>=3.6',
    url='https://github.com/ibrahimhasnat/logsnap/'
)