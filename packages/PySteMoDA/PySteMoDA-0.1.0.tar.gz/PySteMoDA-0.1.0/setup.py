from setuptools import setup, find_packages

setup(
    name='PySteMoDA',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'matplotlib==3.7.0',
        'pandas==1.5.3',
        'ProDy==2.4.0',
        'scikit-learn==1.2.1',
        'seaborn==0.12.2',
        'imageio==2.34.1'
    ],
    description='PySteMoDA',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://gitlab.com/fm4b_lab/smdanalysis',
    author='Ismahene Mesbah',
    author_email='mesbah.ismahene@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8, <3.12',
)

