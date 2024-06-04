from setuptools import setup, find_packages

import setuptools

setuptools.setup(
	name="soda_generator",
	version="0.0.1",
	author="Mira Terekhova",
	author_email="your@email.com",
	description="This is packege designed for auto-generation of contracts and tests in the soda syntax",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.6',
)

