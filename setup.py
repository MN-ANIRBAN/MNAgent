from setuptools import setup, find_packages

setup(
    name="mnagent",
    version="2.4",
    packages=find_packages(),
    author="ANIRBAN ADHIKARY",
    description="A dynamic dependency guard that auto-manages python packages.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://https://github.com/MN-ANIRBAN/MNAgent", # GitHub link
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[], 
)
