from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='cosmic-counsel',
    version='0.1.0',
    author='Collin Paran, Eric Willis',
    url='https://www.boozallen.com/',
    description='Space R&D',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    package_data={"cosmic-counsel": ["models/*", "data/*.json", "data/*.pkl"]},
    entry_points={
        'console_scripts': [
            'cosmic-counsel=cosmic_counsel.__main__:main',
        ],
    },
    install_requires=[
        'torch',
        'transformers',
        'numpy',
        'pandas',
        'uvicorn',
        'bitsandbytes',
        'accelerate',
        'sentence-transformers',
        'nltk',
        'PyPDF2',
        'pydantic',
        'requests',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    license='Apache 2.0',
)
