from setuptools import setup, find_packages

setup(
    name='loopy-auto',
    version='0.0.1-b',
    packages=find_packages(),
    description='Loopy-auto is an automation framework in which anybody can create a test script simply with your favorite language.',
    author='Jooho Lee',
    author_email='ljhiyh@gmail.com',
    url='https://github.com/jooho/loopy',
    install_requires=['automation', 'openshift'],
    keywords=['jooho', 'loopy automation','openshift', 'opendatahub ai' 'pypi'],
    python_requires='>=3.10',
    package_data={},
    zip_safe=False,
    classifiers=[        
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
