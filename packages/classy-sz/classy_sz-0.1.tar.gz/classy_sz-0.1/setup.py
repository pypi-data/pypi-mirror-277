from setuptools import setup,find_packages




setup(
    name="classy_szfast",
    version="0.1",
    description="Python package for fast class_sz",
    zip_safe=False,
    packages=find_packages(),
    author='Boris Bolliet et al',
    author_email='boris.bolliet@gmail.com',
    url='https://github.com/CLASS-SZ/class_sz',
    download_url='https://github.com/CLASS-SZ/classy_szfast',
    install_requires=[
        "tensorflow==2.13.0",
        "tensorflow-probability==0.21.0",
        "cosmopower",
        "mcfit"
    ],
    package_data={},
)
