from setuptools import find_packages, setup

setup(
    name="hello_world_deshitha2",
    version="0.5",
    description="A simple hello world package  and uploading to pypi and adding it o the gitlab version2",
    author="deshi",
    author_email="deshithabollina28@gmail.com",
    packages=find_packages(),
    install_requires=[
        "click",
    ],
    entry_points={
        "console_scripts": [
            "greet=hello_world.cli:greet",
        ],
    },
)
