from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 2 - Pre-Alpha',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='covid19BD',
  version='0.0.1',
  description='It lets you interact with my database created by Covid-19 Bot hosted on repl.it for Bangladesh from 15th January 2021 - Current Day.',
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
  long_description_content_type="text/markdown",
  url='',  
  author='Arib Muhtasim',
  author_email='aribmuhtasim22@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords=['Covid-19', 'Coronavirus'], 
  packages=find_packages(),
  install_requires=['pyrebase', 'json']
)