from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    l_description = f.read()


setup(
    name='metathreadspy',
    version='0.0.0',
    packages=find_packages(),
    install_requires=[
    ],
    description="",
    long_description=l_description,
    long_description_content_type='text/markdown',
)
