"""Setup."""
from setuptools import setup, find_packages

external_modules = []

if __name__ == '__main__':
    setup(
        name='yutils',
        version='0.0.1',
        packages=find_packages(),
        # package_dir={'yutils.log': 'log',
        #              'yutils.timer': 'timer',
        #              'yutils.funs': 'funs'},
        # install_requires=external_modules,
        author='Yu-Yu',
        author_email='hyuyu1544@gmail.com',
        python_requires='>=3.6',
    )
