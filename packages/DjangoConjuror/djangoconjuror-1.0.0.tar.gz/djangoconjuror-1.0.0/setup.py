from setuptools import setup, find_packages

setup(
    name='DjangoConjuror',
    version='1.0.0',
    packages=find_packages(include=['conjuror', 'conjuror.*']),
    install_requires=[
        'django',
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'conjuror = conjuror.cli:main',
        ],
    },
    author='Hassan Farooq',
    author_email='hf537923@gmail.com',
    description='This tool is created to ease the Django Development. Developers can use this to setup their projects easily with just simple commands.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',  # if your README is Markdown
    url='https://github.com/hackeron22/DjangoConjuror',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Framework :: Django',
    ],
)
