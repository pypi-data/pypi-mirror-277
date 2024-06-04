from setuptools import setup


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="korea",
    version="1.1.0",
    author="Joumaico Maulas",
    description="Hangul Romanizer",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/joumaico/korea",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    packages=[
        "hangul",
    ],
    package_dir={
        "hangul": "src/hangul",
    },
    package_data={
        "hangul": [
            "convert/data/latin/*",
            "convert/data/raw/*",
            "convert/data/provisions",
            "convert/output/latin/*",
            "convert/output/raw/*",
        ]
    },
    python_requires=">=3.11",
    install_requires=[
        "numpy",
    ],
)
