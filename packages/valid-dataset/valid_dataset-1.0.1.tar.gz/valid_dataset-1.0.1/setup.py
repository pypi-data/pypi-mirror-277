from setuptools import setup

setup(
    name='valid_dataset',
    version='1.0.1',
    py_modules=['valid_dataset'],
    install_requires=[
        'pyyaml',
    ],
    entry_points={
        'console_scripts': [
            'valid-dataset=valid_dataset:main',
        ],
    },
)
