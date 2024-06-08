from setuptools import setup, find_packages
import os

# Read the contents of the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='social-media-url-extractor',
    version='0.1.1',
    description='A module to extract social media URLs from given URL',
    author='Coopr-AI',
    author_email='coopr-ai@outlook.com',
    url='https://github.com/coopr-ai/social-media-url-extractor/',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'hrequests',
        'beautifulsoup4',
        'pyyaml',
        'click'
    ],
    entry_points={
        'console_scripts': [
            'extract-social-media-urls=social_media_url_extractor.cli:extract',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    long_description=long_description,
    long_description_content_type='text/markdown',
)
