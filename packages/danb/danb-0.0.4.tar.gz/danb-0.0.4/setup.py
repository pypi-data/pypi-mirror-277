from setuptools import setup, find_packages

VERSION = '0.0.4' 
DESCRIPTION = 'danb package'
LONG_DESCRIPTION = 'danb package'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="danb", 
        version=VERSION,
        author="Daniel QBertuzzi",
        author_email="<dqbertuzzi@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'
        
        keywords=['python', 'utils'],
        classifiers= [
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)