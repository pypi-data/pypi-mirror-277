from setuptools import setup, find_packages  

VERSION = '0.1.0'  
DESCRIPTION = 'Open Redirect Bug Finding Tool'
LONG_DESCRIPTION = 'Open Redirect Bug Finding Tool...This tool is designed to detect Open Redirect vulnerabilities in web applications. It parses URLs to identify potential vulnerabilities and provides output in a specified file.'

try:
 with open("README.md", "r", encoding="utf-8") as fh:
   long_description = fh.read()
except FileNotFoundError:
   long_description = LONG_DESCRIPTION

setup(
name="openredirectscanner",
version=VERSION,
author="Snega Prabhavathi.P",
author_email="prabhavathisnega@gmail.com",
description=DESCRIPTION,
long_description=long_description,
long_description_content_type="text/markdown",
packages=find_packages(include=['units', 'packages', 'packages.includes']),
entry_points={
'console_scripts': [
'openredirectscanner = units.main',
    ],
},
install_requires=[
    'requests>=2.25.1',
    'argparse>=1.4.0',
    'termcolor>=1.1.0',
    'pyfiglet>=0.8.post1'
],
classifiers=[
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3.8",
    "Operating System :: OS Independent",
],
python_requires='>=3.8',
include_package_data=True,
)