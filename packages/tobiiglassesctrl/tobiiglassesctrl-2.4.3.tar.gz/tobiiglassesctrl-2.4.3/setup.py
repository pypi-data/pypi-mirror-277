from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='tobiiglassesctrl',
    version='2.4.3',
    description='A Python controller for Tobii Pro Glasses 2',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ddetommaso/TobiiGlassesPyController/',
    download_url='https://github.com/ddetommaso/TobiiGlassesPyController/archive/2.4.3.tar.gz',
    install_requires=['netifaces', 'opencv-python==4.2.0.32', 'av==8.0.3'],
    author='Davide De Tommaso',
    author_email='dtmdvd@gmail.com',
    keywords=['eye-tracker', 'tobii', 'glasses', 'tobii pro glasses 2', 'tobii glasses', 'eye tracking'],
    packages=find_packages(exclude=['examples*']),
    classifiers=[
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ],
)
