from setuptools import setup, find_packages


setup(
	name="automatic_contract_creation",
	version="1.0.0",
	author="Mira Terekhova",
	author_email="miraterekhova@mail.ru",
	description="This is package designed for auto-generation of contracts and tests in the soda syntax",
	packages=find_packages(),
	install_requires=['polars', 'pandas', 'datetime', 'os', 'clickhouse_connect',
					  'connect', 'BasicAuthentication', 're'],
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.7',
)

