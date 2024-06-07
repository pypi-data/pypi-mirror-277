from setuptools import setup, find_packages


setup(
    name="terminal_test",
    version="1.0.2",
    package=find_packages(),
    install_requires=[
        #test
    ],
    entry_points={
        "console_scripts":[
            "hello = terminal:hello"
        ]
    }
)