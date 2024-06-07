from setuptools import setup, find_packages

setup(
    name="email_utils_PyWendi",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    author="RAKOTONDRANAIVO GILBERT Joyaux Wendi Anderson",
    autho_email="rakotondranaivogilbert21@gmail.com",
    description="A python module for validation and generation of email address",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/PyWendi/email_utils_module",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)