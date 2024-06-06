from setuptools import setup, find_packages

setup(
    name='DkFolderManager',
    version='0.0.1',
    description='A simple folder management library using JSON',
    author='dntjd207',
    author_email='dntjd207@naver.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)