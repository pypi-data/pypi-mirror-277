from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='piplink',
    version='1.0.0',
    author='Fidal',
    author_email='mrfidal@proton.me',
    description='piplink is a Python package for uploading packages to PyPI.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://mrfidal.in/basic-pip-package/piplink',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'piplink-upload=piplink.upload:main',
        ],
    },
    install_requires=[
        'requests',
        'requests-toolbelt',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

