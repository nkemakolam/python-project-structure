import  os, sys, re
# get version info from module without importing it
version_re = re.compile("""__version__[\s]*=[\s]*['|"](.*)['|"]""")

with open('hellowworld.py') as f:
    content = f.read()
    match =  version_re.search(content)
    version = match.group(1)
readme = os.path.join(os.path.dirname(__file__), 'README.md')
long_description = open(readme).read()



SETUP_ARGS = dict(
    name='helloword',
    version=version,
    description=('Grab the "Hello World"  Wikkipedia page and print its title'),
    long_description=long_description,
    url='https://github.com/<your login>/hellowworkd',
    author = '<AUTHOR>',
    author_email='<EMAIL',
    license='MIT',
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 -Beta',
        'Envronment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',

    ],

    py_modules = ['helloworld',],
    install_requires=[
        'requests>=2.22',
    ],
)
if __name__ == '__main__':
    from setuptools import setup, find_packages