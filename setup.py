from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Anime Recommendation System",
    version="0.1",
    author="Vishwas",
    packages=find_packages(),
    install_requires = requirements,
)