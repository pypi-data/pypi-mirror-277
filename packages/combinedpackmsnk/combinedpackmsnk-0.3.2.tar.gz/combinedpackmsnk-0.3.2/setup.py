from setuptools import setup, find_packages

setup(
    name='combinedpackmsnk',
    version='0.3.2',  # Increment the version number
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'plotly',
        'scikit-learn',
        'statsmodels',
        'xgboost',
        'ydata-profiling',
        'nbformat'
    ],
    entry_points={
        'console_scripts': [],
    },
    author='mukund14',
    author_email='mukundan.sankar14@gmail.com',
    description='A comprehensive package for data analysis, data visualization, data preprocessing, and machine learning',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/mukund14/combinedpackmsnk',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
