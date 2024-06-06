from setuptools import setup, find_packages

setup(
    name='pipeline_schema_auxo',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'SQLAlchemy',
        'psycopg2-binary',
    ],
    entry_points={
        'console_scripts': [
            # Add any command-line scripts here
        ],
    },
    author='Sujit',
    author_email='sujit.chaurasia@procdna.com',
    description='A description of your package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ProcDNA-Auxo/pipeline_schema_auxo',  # Update with your GitHub URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
