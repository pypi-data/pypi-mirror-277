from setuptools import setup


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="mustasa",
    version="1.1.0",
    author="Joumaico Maulas",
    author_email="joumaico@yahoo.com",
    description="SQL Database Wrapper",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/joumaico/mustasa",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    packages=[
        "mustasa",
    ],
    package_dir={
        "mustasa": "src/mustasa",
    },
    python_requires=">=3.11",
    install_requires=[
        "aiosqlite",
        "asyncpg",
        "psycopg2-binary",
        "pymysql",
    ],
)
