from setuptools import setup, find_packages

setup(
    name='xiao0.0.2',                # The file name of the package after packaging
    version='0.1',              # version number
    author='Xiaofang',
    author_email='1958976685@qq.com',
    url='https://example.com/xiao0.0.2',  # Replace with your actual project URL
    package_dir = {"": "src"},       # The python package directionry
    packages=find_packages(where="src"), # The python package directionry
    install_requires=['simplejson',],    # The pyhon package was required 
)
