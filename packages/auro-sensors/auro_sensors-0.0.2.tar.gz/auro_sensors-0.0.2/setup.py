#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open("README.md") as readme_file:
    readme = readme_file.read()

requirements = [
    'auro_utils',
    'pyrealsense2>=2.54',
    'matplotlib>=3.7',
    'imageio>=2.34',
    'transforms3d>=0.4',
    'opencv-contrib-python>=4.9',
    'opencv-python>=4.9'
]

test_requirements = [
    "pytest>=3",
]

setup(
    author="Herman Ye",
    author_email="hermanye233@icloud.com",
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    description="sensors for auromix application",
    install_requires=requirements,
    include_package_data=True,
    long_description=readme,
    long_description_content_type="text/markdown",
    keywords="auro_sensors",
    name="auro_sensors",
    packages=find_packages(include=["auro_sensors", "auro_sensors.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/Auromix/auro_sensors",
    version="0.0.2",
    zip_safe=False,
)
