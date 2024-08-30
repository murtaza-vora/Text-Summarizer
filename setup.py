import setuptools  # it is require when we need to publish it somewhere so that others can install it and use it

with open("README.md", "r", encoding= "utf-8") as f:
    long_description = f.read()


version = "0.0.0"

REPO_NAME = "Text-Summarizer"
Author_Name = "Murtaza"
SRC_REPO_NAME = "text_summarization"
Author_Email = "voramurtaza2000@gmail.com"


setuptools.setup(
    name = SRC_REPO_NAME,
    version= version,
    author = Author_Name,
    author_email = Author_Email,
    description = "This is a simple Python package for text summarization.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = f"https://github.com/{REPO_NAME}",
    project_urls = { "bug tracker": f"https://github.com/{REPO_NAME}/issues" },
    package_dir= {"" : "src"},
    packages = setuptools.find_packages(where="src")

)
    
