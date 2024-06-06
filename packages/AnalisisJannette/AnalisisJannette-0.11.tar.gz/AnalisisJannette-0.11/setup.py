from setuptools import setup, find_packages

setup(
    name='AnalisisJannette',
    version='0.11',
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
            'manage = manage:main',  # Apunta al archivo manage.py en la raíz del proyecto
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Framework :: Django',
        'Operating System :: OS Independent',
    ],
)
