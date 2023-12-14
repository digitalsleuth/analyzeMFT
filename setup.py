from distutils.core import setup

setup(
    name='analyzeMFT',
    version='3.0.0',
    author='Corey Forman',
    author_email='corey@digitalsleuth.ca',
    packages=['analyzemft'],
    url='http://github.com/digitalsleuth/analyzeMFT',
    license='LICENSE.txt',
    description='Analyze the $MFT from a NTFS filesystem.',
    long_description=open('README.md').read(),
    scripts=['analyzeMFT.py']
)
