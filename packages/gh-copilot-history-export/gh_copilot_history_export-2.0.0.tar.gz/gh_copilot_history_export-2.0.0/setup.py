from setuptools import setup

setup(
    name='gh-copilot-history-export',
    version='2.0.0',
    packages=['che', 'che.intercept'],
    license='LICENCE',
    author='mustafakilic',
    author_email='ben@mustafakilic.com',
    description='Long Description',
    install_requires=[
        'mitmproxy',
        'click',
        'setuptools'
    ],
    entry_points={
        'console_scripts': [
            "che = che.main:main"
        ]
    }
)
