from setuptools import setup, find_packages

setup(
    name="obsn",
    version="1.0.2",
    author="SevenworksDev",
    author_email="mail@sevenworks.eu.org",
    description="Making Geometry Dash tool development easier in Python.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/ObsidianGD/ObsidianPy",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=[
        "requests",
        "plyer",
    ],
)