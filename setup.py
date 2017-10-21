
from setuptools import setup


setup (
    name='Trigrams',
    description='Takes in a source text, then creates a dictionary from the text to create new text.',
    author='Brendan Davis and Phil Werner'
    package_dir={'': 'src'},
    py_modules=['Trigrams'],
    install_requires=[],
    extras_require={
        'testing':['pytest', 'pytest --cov']
        'development':['ipython']
        },
    entry_points={
        'console_scripts':[
            'runme = Trigrams:main'
        ]
        }
    )