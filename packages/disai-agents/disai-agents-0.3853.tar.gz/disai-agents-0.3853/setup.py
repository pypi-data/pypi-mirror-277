# setup.py
from setuptools import setup, find_packages

setup(
    name='disai-agents',
    version='0.3853',
    packages=find_packages(),
    description='A Python library for Easy LLM Agent functionalities.',
    author='DISAI Community',
    author_email='nisarvskp@gmail.com',
    url='https://github.com/raaasin/digiotai',  # Optional
    install_requires=['openai', 'python-dotenv','requests','beautifulsoup4','duckduckgo_search','newspaper3k'],  # List dependencies here if any
)
