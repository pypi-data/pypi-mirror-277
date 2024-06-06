from setuptools import setup, find_packages
setup(
name='sftp_smtp',
# name='sftp-smtp',
# version='1.0.3',
version='1.0.4',
author='Sunesh Pandita',
author_email='suneshpandita2009@gmail.com',
description='This package includes functionality to work with any SFTP and SMTP server',
packages=find_packages(),
classifiers=[
'Programming Language :: Python :: 3',
'License :: OSI Approved :: MIT License',
'Operating System :: OS Independent',
],
python_requires='>=3.10.0',
)