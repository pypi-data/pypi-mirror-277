from setuptools import setup, find_packages

setup(
    name='naowidgets',
    version='0.1.1',
    package_dir={'': 'src'},
    py_modules=['naowidgets'],
    install_requires=[
        'ipywidgets',
        'IPython'
    ],
    platforms="any",
    author='Emile Kroeger',
    author_email='e.kroeger@unitedrobotics.group',
    description='A small library with useful widgets for NAO in Jupyter.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/NaosClassroom/naowidgets',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
