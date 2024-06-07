from setuptools import setup, find_packages

setup(
    name='crisper-ai',
    version='0.3.0',
    author='Crisper Support',
    author_email='support@crisper.ai',
    description='Simple API for creating AI assistants',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/crisperai/python-sdk',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)