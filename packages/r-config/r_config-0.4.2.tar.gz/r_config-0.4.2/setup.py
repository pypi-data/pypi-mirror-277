from setuptools import setup

with open('README.rst', 'r') as f:
    long_description = f.read()

setup(
    name='r_config',
    version="0.4.2",
    packages=['r_config'],
    author="Ramin Zarebidoky",
    author_email="ramin.zarebidoky@gmail.com",
    description="A customized way to use config",
    url="https://github.com/LiterallyTheOne/r_config",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    install_requires=['pyyaml'],
    python_requires='>3.9.0'
)
