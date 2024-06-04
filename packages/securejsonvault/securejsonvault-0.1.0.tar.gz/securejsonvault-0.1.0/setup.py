from setuptools import setup

setup(
    name='securejsonvault', 
    version='0.1.0',
    py_modules=['script'],
    install_requires=[
        'click==8.1.7',
        'cryptography==42.0.7',
        'jinja2==3.1.4',
    ],
    entry_points={
        'console_scripts': [
            'sjv=script:cli',
        ],
    },
    author='Karam T.',  
    author_email='dev@tayyem.eu',  
    description='A simple Python command-line script to securely manage secrets in a JSON keystore file.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/I-Need-C8H10N4O2/SecureJSONVault', 
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
    ],
    python_requires='>=3.10',
    license='GPLv3',
)
