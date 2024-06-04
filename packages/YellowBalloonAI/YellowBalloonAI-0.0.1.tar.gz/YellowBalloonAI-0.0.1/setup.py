from setuptools import setup, find_packages

setup(
    name="YellowBalloonAI",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    author="박재형",
    author_email="crimebbo@ybtour.co.kr",
    description="A ybtour Ai SDK for interacting with an API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/crimebbo/ybai_sdk",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
