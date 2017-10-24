"""For setup."""
from setuptools import setup


setup(
    name='Trigrams',
    description="""Take a source text and create a dictionary from it
    to create new text.""",
    author='Brendan Davis and Phil Werner',
    package_dir={'mail_room_madness.py': 'src'},
    py_modules=['Trigrams'],
    install_requires=[],
    extras_require={'testing': ['pytest', 'coverage']},
        'development': ['ipython']},
    entry_points={
        'console_scripts': [
            'runme = Trigrams:main'
        ]})
