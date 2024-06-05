from setuptools import setup, find_packages

setup(
    name='casablanca_Stock',
    version='1.2.9',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
        'pandas',
        'selenium',
        'streamlit',
        'groq'
    ],
)