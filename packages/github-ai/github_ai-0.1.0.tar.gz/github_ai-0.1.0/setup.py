from setuptools import setup, find_packages

setup(
    name='github-ai',
    version='0.1.0',
    packages=find_packages(),
    install_requires=['requests'],
    entry_points={
        'console_scripts': [
            'github-ai = github_api.__main__:main'
        ]
    },
    author='Fidal',
    author_email='mrfidal@proton.me',
    description='A Python package to interact with GitHub API',
    url='https://mrfida.in',
)
