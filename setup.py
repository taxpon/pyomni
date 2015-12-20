from setuptools import setup
import pyomni

setup(
    name=pyomni.__name__,
    packages=[pyomni.__name__],
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
