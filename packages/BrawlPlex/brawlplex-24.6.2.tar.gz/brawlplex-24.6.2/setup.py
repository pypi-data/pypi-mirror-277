from setuptools import setup, find_packages

setup(
    name='BrawlPlex',
    version='24.6.2',
    author='BrawlAPI Dev',
    author_email='brawlapi.dev@gmail.com',
    description='A package for Brawl Stars API',
    url='https://github.com/yourusername/BrawlPlex',  # Replace with your GitHub repository URL
    packages=find_packages(),
    install_requires=[
        'requests>=2.32.3',  # Example dependency
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.12',
    include_package_data=True,
)