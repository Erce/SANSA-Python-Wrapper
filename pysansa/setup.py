import setuptools
from setuptools import find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pysansa", # Replace with your own username
    version="0.0.1",
    packages=find_packages(),
    #package_data={'': ['SANSA_all_dep_NO_spark.jar','myjars/SANSA_all_dep_NO_spark.jar']},
    include_package_data=True, 
    py_modules=[], 
    author="Pahulmeet Singh, Alexander Krasnobaev, Erce Can Balcioglu",
    description="SANSA Python Wrapper",
    #long_description=long_description,
    #long_description_content_type="text/markdown",
    #url="https://github.com/pypa/sampleproject",
    #classifiers=[
    #    "Programming Language :: Python :: 3",
    #    "License :: OSI Approved :: MIT License",
    #    "Operating System :: OS Independent",
    #],
    #packages=setuptools.find_packages(),
    python_requires='>=3.6',
)
