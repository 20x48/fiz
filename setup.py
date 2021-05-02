from setuptools import setup, find_packages

VERSION = open('fiz/v.py', encoding='utf-8')
README = open('README.md', encoding='utf-8')

setup(
    name='fiz',
    author='20x48',
    author_email='the20x48@outlook.com',
    url='https://github.com/20x48/fiz',
    version=VERSION.readline()[15:-2],
    packages=find_packages(),
    package_data={'fiz': ['i.txt']},
    project_urls={'Github': 'https://github.com/20x48/fiz'},
    python_requires='>=3.6',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    description="A utility use to convert HEX to (i've tried my best) Human.Spellable.Words.",
    long_description=README.read(),
    long_description_content_type='text/markdown'
)

VERSION.close()
README.close()