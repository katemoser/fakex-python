from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='fakex-python',
    version='0.0.3',
    author='Kate Moser',
    author_email='komoser@gmail.com',
    description='Currency conversion with sample data',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/katemoser/fakex-python',
    packages=['fakex-python'],
)