from setuptools import setup, find_packages

setup(
    name='vampgui',
    version='0.1.0',
    author='G. Benabdellah',
    author_email='ghlam.benabdellah@gmail.com',
    description='Interface graphic to vampire "Atomistic simulation of magnetic materials"',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/vampgui',  # Replace with your project's URL
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'vampgui': ['background.png', 'logo.png', 'vam.ico'],
    },
    install_requires=[
        'matplotlib',
        'Pillow',
        'tk',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'vampgui = vampgui.main:main',
        ],
    },
)

