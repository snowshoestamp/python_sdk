import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sssapi-pkg", # Replace with your own username
    version="0.1.0",
    author="Snowshoe Stamps",
    author_email="engineering@snowshoestamp.com",
    description="SnowShoeStamp Client Api Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/snowshoestamp/python_sdk",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
)