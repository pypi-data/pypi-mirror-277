from setuptools import setup, find_packages

setup(
    name='casablanca_Stock',
    version='0.2.7',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
        'pandas',
        'selenium',
        'streamlit'
        'groq'
    ],
)