from setuptools import setup
from setuptools import find_packages
import pyomni

setup(
    name=pyomni.__name__,
    packages=find_packages(exclude=['tests*']),
    version=pyomni.__version__,
    author=pyomni.__author__,
    author_email="taxpon@gmail.com",
    description="Python library to handle omnifocus tasks.",
    url=pyomni.__url__,
    license=pyomni.__license__,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python",
    ]
)
