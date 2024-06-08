from setuptools import setup, find_packages

with open("README.md", 'r') as f:
    description = f.read()

setup(
    name="hey_shbh",
    version = '10.2',
    packages=find_packages(),
    install_requies = [
        "numpy",
        "os",
    ],
    entry_points = {
        "console_scripts" : [
            "hey_shbh = hey_shbh:namaste",
            
        ],
    },
    long_description=description,
    long_description_content_type='text/markdown',
)