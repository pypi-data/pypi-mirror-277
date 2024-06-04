from setuptools import setup, find_packages

setup(
    name="open_parny",
    version="0.1.0",
    packages=find_packages(),
    description="A Python package to send alerts to Parny.io webhooks.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Hasan Aday",
    author_email="hasan@parny.io",
    url="https://github.com/haday23/open-parny.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "requests",
    ],
    python_requires='>=3.6',
)
