from setuptools import setup, find_packages # type: ignore

setup(
    name='morpheus-integration',
    version='0.1.1',
    author='Bruno Moretti',
    url='https://github.com/StafSis/Morpheus-Python-Integration',
    install_requires=[
        'requests; python_version<"3.12"',
    ],
    packages=find_packages(where='src'),
    package_dir={'': 'src'}
)
