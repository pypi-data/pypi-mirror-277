from setuptools import setup

long_description = open('README.md').read()

setup(
   name='my-new-release-project-aba1',
   description='good job',
   long_description_content_type="text/markdown",
   long_description=long_description,
   author='kirill',
   author_email='KARum2004@yandex.ru',
   packages=['package1'],
   install_requires=[]
)