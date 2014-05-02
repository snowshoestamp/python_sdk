from setuptools import setup

setup(
    name="sssapi",
    packages=['sssapi'],
    version='0.0.5',
    author="snowshoestamp",
    license="MIT",
    author_email="hello@snowshoestamp.com",
    url="https://github.com/snowshoestamp/python_sdk",
    description="SnowShoeStamp Client Api Library",
    zip_safe=False,
    include_package_data=True,
    install_requires = [
        'requests_oauthlib',
    ]
)
