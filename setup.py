"""Setup."""
from setuptools import setup, find_packages

external_modules = []

if __name__ == '__main__':
    setup(
        name='yutils',
        version='0.0.5',
        packages=find_packages(),
        author='Yu-Yu',
        author_email='hyuyu1544@gmail.com',
        python_requires='>=3.6',
    )
