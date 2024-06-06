# -*- coding: utf-8 -*-

import setuptools


SOURCE_DIRECTORY = 'src'
with open("README.md", "r", encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()
    f.close()



setuptools.setup(
    name="krxdata",
    version="2.0.0",
    author="innovata",
    author_email="iinnovata@gmail.com",
    description='한국거래소 데이터 API',
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url=f"https://github.com/innovata/KrxDataAPI",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": SOURCE_DIRECTORY},
    packages=setuptools.find_packages(SOURCE_DIRECTORY),
    python_requires=">=3.9",
    install_requires=['ipylib', 'holidays', 'pandas','xlrd', 'openpyxl', 'requests'],
)
