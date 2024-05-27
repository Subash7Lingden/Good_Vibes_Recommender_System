from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "ML Based good_vibes_recommender_system"
AUTHOR_USER_NAME = "Subash7LIngden"
SRC_REPO = "gv_recommender"
LIST_OF_REQUIREMENTS = []


setup(
    name=SRC_REPO,
    version="0.0.1",
    author="Subash7Lingden",
    description="A small local packages for ML based good vibes tracks recommendations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Subash7Lingden/repository-cat-vs-dog/raw/main/zip_recommender%20system.zip",
    author_email="subashsubbalingden@gmail.com",
    packages=find_packages(),
    license="MIT",
    python_requires=">=3.8",
    install_requires=LIST_OF_REQUIREMENTS
)