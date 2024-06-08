from setuptools import setup, find_packages

setup(
    name='ligand_processor',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'parmed',
    ],
    entry_points={
        'console_scripts': [
            'preprocess_ligand=ligand_processor.preprocess_mol2:preprocess_ligand',
            'generate_topology=ligand_processor.generate_top:generate_topology',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A package to preprocess ligand files and generate topology files for GROMACS.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/ligand_processor',  # Replace with your repository URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
