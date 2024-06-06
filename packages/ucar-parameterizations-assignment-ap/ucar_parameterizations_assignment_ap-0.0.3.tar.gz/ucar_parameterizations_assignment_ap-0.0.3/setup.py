from setuptools import setup, find_packages

VERSION = '0.0.3' 
DESCRIPTION = 'Foo et al. parameterization'
LONG_DESCRIPTION = 'UCAR assignment Foo et al. parameterization designed with the task of making an easy to learn and modify shape parameterization package.'

# Setting up
setup(
        name="ucar-parameterizations-assignment-ap", 
        version=VERSION,
        author="Austin Pliska",
        author_email="<ajpliska873t.i@email.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages that 
        
        keywords=['python', 'ucar', 'parameteriazation', 'foo', 'sphere'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)