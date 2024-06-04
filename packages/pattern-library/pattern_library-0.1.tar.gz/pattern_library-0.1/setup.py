from setuptools import setup, find_packages

setup(
    name='pattern_library',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # list your dependencies here
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A description of your package',
    long_description=open('README.txt').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/pattern_library',  # update with your repository URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
