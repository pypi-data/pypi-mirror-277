from setuptools import find_packages, setup

setup(
    name="hello_world_hemanth",
    version="0.17",
    description="A simple Hello package for subtracting two numbers",
    author="Hemanthbollina123",
    author_email="hsbollina@gmail.com",
    packages=find_packages(),
    install_requires=[
        "click",
    ],
    entry_points={
        "console_scripts": [
            "subtract=hello_world.cli:main",
        ],
    },
)
