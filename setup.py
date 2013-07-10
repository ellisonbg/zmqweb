from setuptools import setup, find_packages

setup(
    name = "zmqweb",
    version = "0.1",
    packages = find_packages(),

    install_requires = ['tornado','pyzmq', 'six'],

    author = "Brian Granger",
    author_email = "ellisonbg@gmail.com",
    description = "ZeroMQ based request handlers for Tornado",
    license = "Modified BSD",
    keywords = "ZeroMQ Tornado PyZMQ",
    url = "http://github.com/ellisonbg/zmqweb",
)

