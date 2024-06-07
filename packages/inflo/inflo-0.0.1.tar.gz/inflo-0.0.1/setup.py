from setuptools import setup, find_packages

setup(
    name="inflo",
    version="0.0.1",
    author="Jerric Lyns John",
    author_email="jerric@inflo.dev",
    description="Package to monitor your AI stack",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
