from setuptools import setup

setup(
    name='valid_dataset',
    version='1.0.0',
    py_modules=['task'],
    install_requires=[
        'pyyaml',
    ],
    entry_points={
        'console_scripts': [
            'valid-dataset=valid_dataset:main',
        ],
    },
)
