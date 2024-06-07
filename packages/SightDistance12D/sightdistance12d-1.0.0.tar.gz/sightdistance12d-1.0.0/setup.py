from setuptools import setup, find_packages
from pathlib import Path



#with open("README.md", 'r') as f:
 #   long_description = f.read()


setup(
    name="SightDistance12D",
    version="1.0.0",
    description = "Functions for summerising 12D Sight Stopping Distance reports",
    #long_description=long_description,
    #long_description_content_type='text/markdown',
    long_description="long description",
    packages=find_packages(),
    install_requires=[
        'numpy>=1.26.4',
        'XlsxWriter>=3.2.0',
        'tabulate>=0.9.0',
        'beautifulsoup4>=4.12.3',
        'pandas>=2.2.2',
        'matplotlib>=3.9.0',
    ]
 
)

#python -m build 

#to practice intall <pip install dist/SightDistance12D-1.0.0-py3-none-any.whl --force-reinstall> !!update version number as required
#to check install status <pip list"

