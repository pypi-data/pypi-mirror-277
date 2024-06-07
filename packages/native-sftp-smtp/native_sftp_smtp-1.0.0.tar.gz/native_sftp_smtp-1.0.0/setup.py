from setuptools import setup, find_packages
setup(
name='native_sftp_smtp',
version='1.0.0',
author='Sunesh Pandita',
author_email='suneshpandita2009@gmail.com',
description='This package includes functionality to work with any SFTP and SMTP server',
packages=find_packages(),
classifiers=[
'Programming Language :: Python :: 3',
'License :: OSI Approved :: MIT License',
'Operating System :: OS Independent',
],
python_requires='>=3.5.0',
)