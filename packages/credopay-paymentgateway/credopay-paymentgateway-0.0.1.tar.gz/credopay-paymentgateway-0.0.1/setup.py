from setuptools import setup, find_packages

setup(
    name="credopay-paymentgateway",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    author="Credopay",
    author_email="support@credopay.com",
    description="A payment gateway package for CredoPay",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)