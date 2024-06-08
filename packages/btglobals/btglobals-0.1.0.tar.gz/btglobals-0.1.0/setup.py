from setuptools import setup, find_packages

setup(
    name='btglobals',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'Django>=3.0',
    ],
    include_package_data=True,
    description='A package containing Django models',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/bugratemirci/python_global',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)