from setuptools import setup, find_packages

setup(
    name='django_internationalization',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        "setuptools>=69.5.1", 
        "Django>=5.0.4", 
        "numpy>=1.26.4", 
        "openpyxl>=3.1.2", 
        "pandas>=2.2.2", 
        "polib>=1.2.0", 
        "XlsxWriter>=3.2.0", 
        "xlwt>=1.3.0"
    ],
)