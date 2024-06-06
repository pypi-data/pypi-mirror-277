from setuptools import setup, find_packages

setup(
    name='nvl',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'nvl=nvl.cli:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A CLI tool to initialize and open directories.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/nvl',  # Replace with your GitHub repo URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
