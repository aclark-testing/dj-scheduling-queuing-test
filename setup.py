from setuptools import find_packages
from setuptools import setup


setup(
    entry_points={
    },
    include_package_data=True,
    install_requires=[
        'Django',
        'requests',
        'rq',
    ],
    name='',
    namespace_packages=[
    ],
    packages=find_packages(),
)
