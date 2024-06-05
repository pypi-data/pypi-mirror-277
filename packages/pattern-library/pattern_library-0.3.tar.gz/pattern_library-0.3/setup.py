from setuptools import setup, find_packages

setup(
    name='pattern_library',
    version='0.3',
    packages=find_packages(),
    install_requires=[
        # list your dependencies here
    ],
    author='Praneeth',
    author_email='pr1neethbv@gmail.com',
    description='A description of your package',
    long_description=open('README.txt').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/pr1neeth/pattern_library',  # update with your repository URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
