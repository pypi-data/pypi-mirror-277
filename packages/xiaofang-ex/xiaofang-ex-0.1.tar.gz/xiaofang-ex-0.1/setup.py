from setuptools import setup, find_packages

setup(
    name='xiaofang-ex',                # The file name of the package after packaging
    version='0.1',              # version number
    author='Xiaofang',
    author_email='1958976685@qq.com',
    url='https://example.com/xiaofang-ex',  # Replace with your actual project URL
    package_dir = {"": "xiaoEx"},       # The python package directionry
    packages=find_packages(where="xiaoEx"), # The python package directionry
    install_requires=['simplejson',],    # The pyhon package was required 
)
