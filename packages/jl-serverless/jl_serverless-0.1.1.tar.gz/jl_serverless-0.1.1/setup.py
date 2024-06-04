from setuptools import setup, find_packages

setup(
    name='jl-serverless',
    version='0.1.1',
    author='Arunkumar',
    author_email='arun19ict@gmail.com',
    description='A CLI tool to run scripts on a remote server.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Arunkumar-Dhanraj/JL-Serverless.git',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=[
        'click',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'jl-serverless=jl_serverless.cli:send_script'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
