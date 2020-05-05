from setuptools import setup

setup(
	name='tensorvault',
	version='0.1.0',
	author='Jonathan Hanna',
	packages=['tensorvault'],
	license='LICENSE.txt',
	description='A modular and expressive interface for managing data in Python',
	long_description=open('README.md').read(),
	install_requires=[
        "numpy >= 1.15.0",
	],
)
