from setuptools import setup, find_packages

setup(
    name='modrinth_downloader',
    version='0.5',
    author='Alexander Brightwater',
    description="Download projects modrinth",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',
    install_requires=[
        'requests',
        'toml',
        'argparse',
    ],
    entry_points={
        'console_scripts': [
            'modrinth_downloader=scripts.run_downloader:main',
        ],
    },
    package_data={
        '': ['config.toml'],  # Include the config.toml file
    },
    include_package_data=True,

)
