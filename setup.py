from setuptools import setup, find_packages

setup(
    name="unapt",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "unapt=unapt.unapt:main",
        ],
    },
    author="Fidal",
    author_email="mrfidal@proton.me",
    description="A Command-Line Package Management Tool for downloading, installing, updating, removing, and managing files.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Tony-Linux/unapt",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires=">=3.6",
)
