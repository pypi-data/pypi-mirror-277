import setuptools

setuptools.setup(
    name='sqlog',
    version='1.3',
    author='Andriy Stremeluk',
    author_email='astremeluk@gmail.com',
    description='Hierarchical logging',
    license='MIT',
    py_modules=['sqlog'],
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [
            'sqlog = sqlog:main',
        ]
    }
)
