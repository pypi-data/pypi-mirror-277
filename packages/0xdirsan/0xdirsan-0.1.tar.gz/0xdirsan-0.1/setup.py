from setuptools import setup, find_packages

# Read the contents of README.md for the long description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="0xdirsan",  
    version="0.1",
    packages=find_packages(),
    description="0xdirsan is a simple program designed to search for directories in the file system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="X-Projetion",
    author_email="lutfifakee@proton.me",
    url="https://github.com/X-Projetion/0xdirsan",
    project_urls={
        "Documentation": "https://github.com/X-Projetion/0xdirsan/wiki",
        "Source Code": "https://github.com/X-Projetion/0xdirsan",
        "Bug Tracker": "https://github.com/X-Projetion/0xdirsan/issues",
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Topic :: Security :: Cryptography",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    keywords="directory search tool filesystem",
    python_requires='>=3.6',
    install_requires=[
        'requests',
        'argparse',
        'colorama',
    ],

    entry_points={
    'console_scripts': [
        '0xdirsan=0xdirsan:main',
    ],
},
)
