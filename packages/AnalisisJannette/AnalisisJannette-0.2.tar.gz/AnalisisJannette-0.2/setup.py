from setuptools import setup, find_packages

setup(
    name='AnalisisJannette',
    version='0.2',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=3.0',
        'sweetify',
        'django-bootstrap5',
        'pandas',
        'unicodedata2',
        'cdifflib',
        # Otros paquetes requeridos
    ],
    entry_points={
        'console_scripts': [
            'manage = my_django_app.manage:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Framework :: Django',
        'Operating System :: OS Independent',
    ],
)
