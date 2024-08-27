from setuptools import setup

setup(
    name='sumTwoNums',
    version='0.1',
    py_modules=['sumTwoNums'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'sumTwoNums=sumTwoNums:main',
        ],
    },
)
