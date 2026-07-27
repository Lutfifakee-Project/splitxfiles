from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="splitxfiles",
    version="0.1.0",
    author="Lutfifakee",
    author_email="lutfifakeeproject@proton.me",
    description="A simple tool to split files into smaller parts based on line count or file size",
    project_urls={
        "Homepage": "https://github.com/Lutfifakee-Project/splitxfiles",
        "Source": "https://github.com/Lutfifakee-Project/splitxfiles",
        "Bug Reports": "https://github.com/Lutfifakee-Project/splitxfiles/issues",
        "Documentation": "https://github.com/Lutfifakee-Project/splitxfiles#readme",
    },
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Lutfifakee-Project/splitxfiles",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Utilities",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "splitxfiles=splitxfiles.cli:main",
        ],
    },
)
