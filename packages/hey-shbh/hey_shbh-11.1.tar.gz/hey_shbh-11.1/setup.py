from setuptools import setup, find_packages

with open("README.md", 'r') as f:
    description = f.read()

setup(
    name="hey_shbh",
    version = '11.1',
    packages=find_packages(),
    install_requies = [
        "numpy",
        "os",
    ],
    entry_points = {
        "console_scripts" : [
            "namaste = hey_shbh:namaste",
            "print_kardo = hey_shbh:print_kardo",
        ],
    },
    long_description=description,
    long_description_content_type='text/markdown',
)