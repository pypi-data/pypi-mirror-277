from setuptools import setup, find_packages

setup(
    name='foo_parameterization_vandit',  
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    description='Package to calculate the Foo et al. parameterization for a sphere.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Vandit Jain',
    author_email='vanditjain19@gmail.com',
    url='https://github.com/vandit1920/foo_parametrization',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
