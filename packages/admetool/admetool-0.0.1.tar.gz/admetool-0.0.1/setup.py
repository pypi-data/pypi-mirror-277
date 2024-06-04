from setuptools import setup, find_packages
import pathlib

setup(name='admetool',
    version='0.0.1',
    license='MIT License',
    author='Júlio César Xavier',
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    author_email='jcaxavier2@gmail.com',
    keywords='admetlab',
    description=u'Tool that uses Pharmit data to perform an ADMET analysis',
    packages= find_packages(),
    install_requires=["pandas==2.2.2","chembl-webresource-client==0.10.9","requests==2.32.3"])