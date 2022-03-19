from setuptools import setup, find_packages
import pathlib

# Get path to parent folder
here = pathlib.Path(__file__).parent.resolve()

# long_description = README.md
long_description = (here / 'README.md').read_text(encoding='utf-8')

github = 'https://github.com/emersonfelipesp/netbox-zabbix'

setup(
    name="netbox-zabbix",
    version="0.0.1",
    author="Emerson Felipe",
    author_email="emersonfelipe.2003@gmail.com",
    description="Netbox and Zabbix integration through API",
    url=github,
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
	    "Framework :: Django",
	    "Operating System :: Unix",
        "License :: OSI Approved :: Apache Software License",
    ],
    keywords="netbox netbox-plugin plugin zabbix zabbix-api api",
    project_urls={
        'Source': github,
    },
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "": ['*','*/*','*/*/*'],
    },
    install_requires=requires,
    extras_require={
        "dev": dev_requires,
    },
    python_requires= '>=3.6',
)