from setuptools import setup, find_packages

setup(
   name='main',
   version='1.0',
   description='prime number checker',
   license='MIT',
   author='smmtoper',
   author_email='sibslav789@gmail.com',
   url='https://github.com/smmtoper/setap',
   packages=find_packages(),
   install_requires=[], # it is empty since we use standard python library
   extras_require={
        'test': [
            'pytest',
            'coverage', 
        ],
   },
   python_requires='>=3',
)