from setuptools import setup, find_packages

setup(
    name="apache-airflow-dragdrop-plugin",
    version="1.1.0",
    description="A custom Apache Airflow plugin to integrate a React UI",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/datainteg/apache-airflow-dragdrop-plugin",
    author="Akshay Thakare",
    author_email="thakarea686@gmail.com",
    packages=["apache_airflow_dragdrop_plugin"],
    include_package_data=True,
    license="Apache License, Version 2.0",
    install_requires=[
        "apache-airflow>=2.0.0",
        "flask"
    ],
    entry_points={
        "airflow.plugins": [
            "apache_airflow_dragdrop_plugin = airflow_dragdrop_plugin.plugin:MyReactPlugin"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Apache Airflow",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3",
)
