"""Setup."""
from setuptools import setup, find_packages

external_modules = []

if __name__ == '__main__':
    setup(
        name='yutils',
        version='0.0.0',
        packages=find_packages(),
        install_requires=external_modules,
        author='Yu-Yu',
        author_email='hyuyu1544@gmail.com',
    )
