import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="borgbase-api-client",
    version="0.0.1",
    author="Borgbase",
    author_email="hello@borgbase.com",
    description="GraphQL client to execute operations against your BorgBase.com account.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/borgbase/borgbase-api-client",
    install_requires=[
        "requests>=2.21.0"
    ],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: System :: Archiving :: Backup"
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
