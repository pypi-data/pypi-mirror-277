from setuptools import setup, find_packages

setup(
    name='viki3lang',  
    version='1.2.0',
    py_modules=['translator'],
    install_requires=[
        'requests',
        'win10toast',
        'googletrans==3.1.0a0',
        'pypiwin32',
        'setuptools'
    ],
    entry_points='''
        [console_scripts]
        viki3lang=translator:main
    ''',
    packages=find_packages(),
)