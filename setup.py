from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """This function will return the list of requirements"""
    requirements_lst:List[str] = []
    try:
        with open("requirements.txt","r") as file:
            lines=file.readlines()

        for line in lines:
            requirement = line.strip()
            if requirement and not requirement!= '-e .':
                requirements_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirements_lst
setup(
    name="networksecurity",
    version="0.0.1",
    author="dharani kumar",
    author_email="dharani.kumar@example.com",
    packages=find_packages(),
    install_requires=get_requirements()
)