from setuptools import find_packages, setup

setup(
    name="animal_detection",
    version="0.1",
    description="A package for animal detection and data scraping",
    author="Your Name",
    packages=find_packages(include=["animal_detection", "animal_detection.*"]),
    install_requires=[
        # list package dependencies, e.g., 'requests', 'beautifulsoup4', etc.
    ],
)
