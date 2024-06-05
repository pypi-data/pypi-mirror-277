from setuptools import setup, find_packages

setup(
    name='xiaoExample',                # The file name of the package after packaging
    version='0.1',              # version number
    author='Xiaofang',
    author_email='1958976685@qq.com',
    url='https://example.com/xiaoExample',  # Replace with your actual project URL
    package_dir = {"": "src"},       # The python package directionry
    packages=find_packages(where="src"), # The python package directionry
    install_requires=['simplejson',],    # The pyhon package was required 
)
