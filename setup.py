from setuptools import setup, find_packages

setup(
    name="apache-airflow-dragdrop-plugin",
    version="0.1.0",
    description="A custom Apache Airflow plugin to integrate a React UI",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/datainteg/apache-airflow-dragdrop-plugin",
    author="Akshay Thakare",
    author_email="thakarea686@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "apache-airflow>=2.0.0",
        "flask"
    ],
    entry_points={
        "airflow.plugins": [
            "drag_drop = my_airflow_plugin.plugin:AirflowDragDropPlugin"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Apache Airflow",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3",
)
