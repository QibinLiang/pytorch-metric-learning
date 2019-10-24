import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pytorch_metric_learning",
    version="0.9.1",
    author="Kevin Musgrave",
    author_email="tkm45@cornell.com",
    description="A flexible and extensible metric learning library, written in PyTorch.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TakeshiMusgrave/pytorch_metric_learning",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)