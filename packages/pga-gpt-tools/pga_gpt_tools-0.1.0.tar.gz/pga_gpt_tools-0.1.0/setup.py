from setuptools import setup, find_packages

setup(
    name='pga_gpt_tools',
    version='0.1.0',
    author='PGA Tech',
    author_email='pgatech@pgahq.com',
    description='A collection of tools for PGA AI products',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/pgahq/pga-gpt-tools',
    packages=find_packages(),
    install_requires=[
        'requests',
        'pydantic',
        'instructor',
        'google-search-results', # web search (serpapi)
        'firecrawl-py', # web scrape
        'fal-client', # transform image
        'openai' # generate image
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
