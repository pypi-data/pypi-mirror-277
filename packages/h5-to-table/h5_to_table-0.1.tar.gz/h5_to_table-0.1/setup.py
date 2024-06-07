from setuptools import setup, find_packages

setup(
    name='h5_to_table',
    version='0.1',
    packages=find_packages(),
    author='H5_To_TABLE Like a Boss-TEAM',
    author_email='ying.xu@unsw.edu.au',
    description='Read in a .h5 file and convert it into a table',
    long_description=open('README.md').read(),
    url='https://github.com/YingX97/H5_to_table',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.6',
)