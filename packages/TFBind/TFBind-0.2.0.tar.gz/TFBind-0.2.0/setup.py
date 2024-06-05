from setuptools import setup, find_packages

setup(
    name="TFBind",
    version="0.2.0",
    author="JingPeng Liu",
    author_email="15313226223@163.com",
    description="Predict whether the transcription factor protein sequence binds to the DNA gene sequence",
    long_description=open('README.md', encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/jingpengLiu/TFBind",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11',
    install_requires=[
        # List your package dependencies here, for example:
        # "numpy >= 1.18.0",
    ],
)