import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="testjaehyun",  ## 소문자 영단어
    version="0.0.3_beta",  ##
    author="Jaehyun Yim",  ## ex) Sunkyeong Lee
    author_email="jhyim@cerestechs.com",  ##
    description="test package distribution",  ##
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    license="",
    url="",
)
