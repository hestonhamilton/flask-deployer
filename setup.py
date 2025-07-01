from setuptools import setup, find_packages

setup(
    name="flask-deployer",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "flask-deployer = flask_deployer.__main__:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)

