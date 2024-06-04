from setuptools import setup, find_packages

setup(
    name='jl-serverless',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'click',  
        'requests',
        'fastapi',
        'uvicorn'
    ],
  entry_points={
    'console_scripts': [
        'jl-cli-tool=main:send_script'  # Here, 'main' is the name of the Python file and 'main' after the colon is the function to execute.
    ]
},
    author='Arunkumar',
    author_email='arun19ict@gmail.com',
    description='A simple CLI tool to run scripts remotely in JarvisLabs.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Arunkumar-Dhanraj/JL-Serverless.git'
)
