from setuptools import setup, find_packages

with open("README.md", "r") as r:
    desc = r.read()

with open("LICENSE", "r") as l:
    lice = l.read()

description = 'PyNeuralNet is a python library for prototyping and building neural networks. PyNeuralNet uses PyTorch as a computational backend for deep learning models.'

setup(
    name='PyNeuralNet',
    version='0.0.4',
    author='ItzLoghotXD',
    author_email='loghot.gamerz.official@gmail.com',
    maintainer='ItzLoghotXD',
    maintainer_email='loghot.gamerz.official@gmail.com',
    description=description,
    long_description=desc,
    long_description_content_type="text/markdown",
    license=lice,
    packages=find_packages(),
    install_requires=[
        'torch==2.1.1',
        'torchvision==0.16.1'
    ],
    url='https://github.com/ItzLoghotXD/neural-network-python',
    download_url='https://pypi.org/project/neural-network-python/',
    keywords=['neural', 'network', 'ai', 'neural network', 'algorithm', 'loghot']
)
