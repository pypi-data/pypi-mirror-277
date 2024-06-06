from setuptools import setup, find_packages

setup(
    name="fast_error_saver",
    version="0.2.0",
    author="Yj Lin",
    author_email="yjlin2001@gmail.com",
    description="Auto save checkpoints when you code raise some exception.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Yu-Jie1669/checkpointer",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "numpy",
    ],
)
