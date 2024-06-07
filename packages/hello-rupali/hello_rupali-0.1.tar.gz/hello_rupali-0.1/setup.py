from setuptools import setup, find_packages

with open("README.md", 'r') as f:
    description = f.read()

setup(
    name="hello_rupali",
    version = '0.1',
    packages=find_packages(),
    install_requies = [
        "numpy",
        "os",
    ],
    entry_points = {
        "console_scripts" : [
            "hello_rupali = hello_rupali:rename_and_copy_with_incremental_index",
        ],
    },
    long_description=description,
    long_description_content_type='text/markdown',
)