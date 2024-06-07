from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    '''
    list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]
    return requirements

setup(
    name='eegAudioAnotator',
    version='1.0.0',
    author='Owais Mujtaba Khanday',
    author_email='owais.mujtaba123@gmail.com',
    url='https://github.com/owaismujtaba/EEGAnotator',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10.14',
    
    entry_points={
        'console_scripts': [
            'eeganotate=eegAudioAnotator.main:main',
        ],
    },
    include_package_data=True,
    package_data={
        '': ['*.msg'],  # Adjust file extensions as needed
        'classes': ['*.msg'],
        'gui': ['*.msg'],
    },
    license='GPL-3.0'
)
