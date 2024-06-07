from setuptools import setup, find_packages

setup(
    name="flaskdev",
    version="0.0.1",  # Adjust the version as needed
    description="Tool to create a basic Flask project structure",
    author="Daniel Beukes",
    packages=find_packages(),
    install_requires=[],  # No external dependencies for this simple setup
    entry_points={
        "console_scripts": [
            "flaskdev = flaskdev.install:main",  # Map the 'flaskdev' command to your script
        ]
    },
)