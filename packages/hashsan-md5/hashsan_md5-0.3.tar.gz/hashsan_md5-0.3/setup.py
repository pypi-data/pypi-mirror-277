from setuptools import setup, find_packages

# Read the contents of README.md for the long description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="hashsan-md5",  
    version="0.3",
    packages=find_packages(),
    description="HashSan: Wordlist-based Password Cracking Tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="X-Projetion",
    author_email="lutfifakee@proton.me",
    url="https://github.com/X-Projetion/hashsan",
    project_urls={
        "Documentation": "https://github.com/X-Projetion/hashsan/wiki",
        "Source Code": "https://github.com/X-Projetion/hashsan",
        "Bug Tracker": "https://github.com/X-Projetion/hashsan/issues",
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
    keywords="hash lookup MD5 cryptography security",
    python_requires='>=3.6',
    install_requires=[
    "argparse",
    "rich",
    "colorama",
    ],

    entry_points={
        'console_scripts': [
            'hashsan=hashsan:main',
        ],
    },
)
