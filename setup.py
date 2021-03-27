import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="untitled-file-organiser",
    version="0.0.1",
    author="TR33HGR",
    author_email="",
    description="A package with scripts for organising you music files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TR33HGR/untitled-file-organiser",
    project_urls={
        "Bug Tracker": "https://github.com/TR33HGR/untitled-file-organiser/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=[
          'pathlib',
    ],
    python_requires=">=3.6",
)