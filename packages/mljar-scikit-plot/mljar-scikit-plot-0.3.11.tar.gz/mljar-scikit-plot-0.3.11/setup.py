from __future__ import print_function
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import io
import codecs
import os
import sys

here = os.path.abspath(os.path.dirname(__file__))


def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

long_description = read('README.md')
# long_description = ''


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

setup(
    name='mljar-scikit-plot',
    version='0.3.11',
    url='https://github.com/mljar/mljar-scikit-plot',
    license='MIT License',
    author='MLJAR Sp. z o.o.',
    tests_require=['pytest'],
    install_requires=[
        'matplotlib>=1.4.0',
        'scikit-learn>=1.1.0',
        'joblib>=0.10'
    ],
    cmdclass={'test': PyTest},
    author_email='contact@mljar.com',
    description='An intuitive library to add plotting functionality to scikit-learn objects.',
    long_description=long_description,
    packages=['scikitplot'],
    include_package_data=True,
    platforms='any',
    test_suite='scikitplot.tests.test_scikitplot',
    python_requires='>=3.9',
    classifiers = [
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Visualization',
        ],
    extras_require={
        'testing': ['pytest'],
    }
)
