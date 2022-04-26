import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='ts4_codegen',
    version='0.0.1',
    author='Vadim Rusakov',
    description='Classes generator for ts4',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://vcs.modus-ponens.com/ton/ts4_codegen',
    packages=['ts4_codegen'],
    install_requires=['jinja2'],
)