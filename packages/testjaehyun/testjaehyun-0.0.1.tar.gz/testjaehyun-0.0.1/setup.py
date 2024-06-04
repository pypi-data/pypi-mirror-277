import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="testjaehyun",  ## 소문자 영단어
    version="0.0.1",  ##
    author="Jaehyun Yim",  ## ex) Sunkyeong Lee
    author_email="jhyim@cerestechs.com",  ##
    description="test package distribution",  ##
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Yimjaehyun93/testjaehyun.git",  ##
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
