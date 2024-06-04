
from setuptools import setup, find_packages

setup(
    name='arion_library',
    version='1.1rc111.dev111',  
    author='Heni Nechi',  
    author_email='h.nechi@arion-tech.com',  
    url='https://github.com/Ariontech/ArionLibrary.git',  
    packages=find_packages(),  
    python_requires='>=3.8',  
    install_requires=['azure-core==1.30.1', 'azure-data-tables==12.5.0', 'azure-storage-blob==12.20.0', 'certifi==2024.2.2', 'cffi==1.16.0', 'charset-normalizer==3.3.2', 'cryptography==42.0.7', 'exceptiongroup==1.2.1', 'idna==3.7', 'iniconfig==2.0.0', 'isodate==0.6.1', 'multidict==6.0.5', 'packaging==24.0', 'pluggy==1.5.0', 'pycparser==2.22', 'pytest==8.2.1', 'python-dotenv==1.0.1', 'requests==2.32.2', 'six==1.16.0', 'tomli==2.0.1', 'typing-extensions==4.12.0', 'urllib3==2.2.1', 'pyodbc', 'pytest', 'Brotli==1.1.0', 'cffi==1.16.0', 'cssselect2==0.7.0', 'defusedxml==0.7.1', 'fonttools==4.52.4', 'fpdf2==2.5.5', 'html5lib==1.1', 'jinja2==3.1.4', 'MarkupSafe==2.1.5', 'pdfkit==1.0.0', 'pillow==10.3.0', 'pycparser==2.22', 'pydyf==0.10.0', 'pypdf2==3.0.1', 'pyphen==0.15.0', 'six==1.16.0', 'tinycss2==1.3.0', 'typing-extensions==4.12.0', 'weasyprint==61.2', 'webencodings==0.5.1', 'zopfli==0.2.3', 'pytest', 'responses', 'pysftp==0.2.9', 'requests==2.31.0', 'azure-data-tables==12.5.0', 'pandas==2.2.2', 'pytest'],
)