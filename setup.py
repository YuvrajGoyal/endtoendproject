from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path):
    HYPHEN_E_DOT='-e .'
    package_name=[]
    with open(file_path) as file_obj:
        package_name=file_obj.readlines()
        ##print(file_line)
        package_name=[req.replace("\n", "") for req in package_name]
        if HYPHEN_E_DOT in package_name:
            package_name.remove(HYPHEN_E_DOT)
    return package_name


setup(
    name='endtoendproject',
    version='0.0.1',
    author='Yuvraj',
    author_email='gyuvvi@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)