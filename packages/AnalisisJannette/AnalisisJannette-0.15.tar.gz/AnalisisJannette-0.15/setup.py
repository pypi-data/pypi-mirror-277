from setuptools import setup, find_packages

setup(
    name='AnalisisJannette',
    version='0.15',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=3.0',
        'sweetify',
        'django-bootstrap5',
        'pandas',
        'unicodedata2',
    ],
    entry_points={
        'console_scripts': [
            'manage = analisisJannette.manage:main',  # Asegúrate de que el nombre del módulo sea correcto
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Framework :: Django',
        'Operating System :: OS Independent',
    ],
)
