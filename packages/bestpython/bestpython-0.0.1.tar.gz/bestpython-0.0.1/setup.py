from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="bestpython",
    version="0.0.1",
    author="MultiFunkIm Lab",
    author_email="ilian@iazz.fr",
    description="A python wrapper for the MEM source method",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ilianAZZ/best-python",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        # "some_dependency>=1.0.0"
    ],
)
