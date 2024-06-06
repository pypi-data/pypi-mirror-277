from setuptools import setup, find_packages

setup(
    name="zerotrust",
    version="0.1.0",
    description="A Python package for interacting with FastAPI endpoints",
    author="sohaib anwar",
    author_email="ysohaib@example.com",
    packages=find_packages(),
    install_requires=["fastapi", "requests"],
)
