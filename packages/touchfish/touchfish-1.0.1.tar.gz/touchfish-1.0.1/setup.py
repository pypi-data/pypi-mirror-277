from setuptools import setup, find_packages

setup(
    name='touchfish',
    version='1.0.1',
    description='data service and python sdk for touchfish #b7ddf862598f2eaffc0c3b6755180abae489944d',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='yzjsswk',
    author_email='yzjsswk@gmail.com',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',
    install_requires=[
        'yfunc'
    ],
)
