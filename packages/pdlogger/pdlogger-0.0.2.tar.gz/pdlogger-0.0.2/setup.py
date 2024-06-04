from setuptools import setup, find_packages

setup(
    name="pdlogger",
    version="0.0.2",
    packages=find_packages(),
    install_requires=["mysql-connector-python==8.4.0","pika==0.13.0"],
    author="parallelldots",
    author_email="dsteam-wiki@paralleldots.com",
    description="An example package",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/yourusername/example_package",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
