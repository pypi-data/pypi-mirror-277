from setuptools import setup, find_packages

setup(
    name='Helix-Engine-TEST',
    version='0.1.0',
    description='THE python game engine',
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/Zero-th/Helix',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'moderngl',
        'glfw',
        'pyrr',
        'numba'
    ],
    classifiers=[
        'Programming Language :: Python :: 3.12',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
