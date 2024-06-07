from setuptools import setup, find_packages

setup(
    name='fixernb',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'nbformat',
    ],
    entry_points={
        'console_scripts': [
            'run-updater=fixernb.fixer:fixer',
        ],
    },
    author='Ashkan Ahmadi',
    author_email='netblag.dev@gmail.com',
    description='A tool to update Jupyter notebooks to version 4',
    url='https://github.com/netblag/jupyter-notebook-fixer',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
