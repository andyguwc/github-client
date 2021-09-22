import io
import re

from setuptools import find_packages
from setuptools import setup

with io.open("ghc/__init__.py", "rt", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

INSTALL_REQUIREMENTS = [
    'click>=7.0',
    'requests>=2.0',
]

EXTRA_REQUIREMENTS = {
    'docs': [
        'sphinx',
    ],
}

setup(
    name='github-client',
    version=version,
    url='https://github.com/andyguwc/github-client',
    license='MIT',
    author='Tianyou Gu',
    author_email='tianyou.gu@gmail.com',
    description='CLI for Github',
    long_description=__doc__,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=INSTALL_REQUIREMENTS,
    setup_requires=[
        'setuptools',
        'wheel',
    ],
    extras_require=EXTRA_REQUIREMENTS,
    entry_points={
        'console_scripts': [
            'ghc = ghc.cli:cli',
        ],
    },
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ]
)
