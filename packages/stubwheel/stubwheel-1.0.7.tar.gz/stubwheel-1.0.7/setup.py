import os
from setuptools import setup, find_packages

setup(
    name='stubwheel',
    version='1.0.7',
    url='https://github.com/AlyShmahell/stubwheel',
    author='AlyShmahell',
    author_email='',
    description='a script that reserves a project name on PyPi',
	long_description=(open('README.md', encoding='utf-8').read() if os.path.exists('README.md')
                        else ''),
    long_description_content_type='text/markdown',
    packages=['stubwheel'],    
    install_requires=['twine >= 3.2.0', 'wheel >= 0.43.0'],
    entry_points = {
        "console_scripts": [
            "stubwheel = stubwheel.__main__:main",
        ]
    }
)