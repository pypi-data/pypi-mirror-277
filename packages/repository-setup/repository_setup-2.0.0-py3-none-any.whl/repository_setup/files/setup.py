from setuptools import setup, find_packages

with open("README.md", "r") as r:
    desc = r.read()

setup(
    name="Insert Name here...", # This name is used in: pip install hello-world
    version="1.0.0",
    author="5f0",
    url="https://github.com/5f0ne/repo-name",
    description="Insert description here...",
    classifiers=[
        "Operating System :: OS Independent ",
        "Programming Language :: Python :: 3 ",
        "License :: OSI Approved :: MIT License "
    ],
    license="MIT",
    long_description=desc,
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=find_packages(where='src'),
    include_package_data=True,
    package_data={
        "repository_setup.files": ["Add files here...."]
    },
    install_requires=[
        "Add dependencies here..."
    ],
     entry_points={
        "console_scripts": [
            "repo-name = repo-name.__main__:main"
        ]
    }
)
