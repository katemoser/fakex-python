import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='fakex-python',
    version='0.0.1',
    author='Kate Moser',
    author_email='komoser@gmail.com',
    description='Currency conversion with sample data',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/katemoser/fakex-python',
    project_urls = {},
    license='',
    packages=['fakex-python'],
    install_requires=['requests'],
)