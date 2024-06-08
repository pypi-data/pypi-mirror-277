from setuptools import setup, find_packages

setup(
    name="pplx",
    version="0.1.3",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "pplx=pplx.cli:main",
        ],
    },
    author="Yannic Basin",
    author_email="yannicbasin@gmail.com",
    description="Ein Hilfsmodul für die Perplexity API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Cinnay1621/pplx",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)