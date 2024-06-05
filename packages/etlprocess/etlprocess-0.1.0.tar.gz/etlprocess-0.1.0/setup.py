from setuptools import setup, find_packages

setup(
    name='etlprocess',
    version='0.1.0',
    author='Jian Zheng', 
    author_email='zhengjian518@outlook.com', 
    packages=find_packages(),
    install_requires=[
        'pyspark',
    ]
)
