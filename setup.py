import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='serial-j',
    version='1.1.6',
    author='Andrew Ray',
    author_email='andrew.ray2@target.com',
    description='Creating a serializer for data structures',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://git.target.com/InfraServices-Storage/serial-j',
    license='MIT',
    packages=setuptools.find_packages(),
    install_requires=[
        'flask-sqlalchemy',
        'sqlalchemy'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
