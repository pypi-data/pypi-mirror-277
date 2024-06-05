from setuptools import setup, find_packages

setup(
    name='Swarm-ECS',
    version='1.0.0.2024-1',
    description='A Flexible Light-Weight Object-Oriented ECS',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Izaiyah Stokes',
    author_email='zeroth.bat@gmail.com',
    url='https://github.com/Zero-th/Swarm',
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3.12',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
)
