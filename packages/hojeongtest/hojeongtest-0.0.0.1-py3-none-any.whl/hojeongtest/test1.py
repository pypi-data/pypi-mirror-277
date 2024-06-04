def print_test1():

    print("hi,this is test1.py page!")

from setuptools import setup, find_packages


setup(name='hojeong',
version='0.0.0.1',
description='My First Test Package',
author='Sukjae Choi',
author_email='hojeongi87@gmail.com',
url='https://lingua.blog.me/…',
license='MIT',
py_modules=['test1', 'test2'],
python_requires='>=3',
packages=['hojeongtest'])
