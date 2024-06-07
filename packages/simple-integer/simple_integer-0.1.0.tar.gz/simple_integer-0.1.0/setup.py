from setuptools import setup

setup(
    name='simple_integer',
    version='0.1.0',
    description='Go to invariantlabs.ai to make your agent secure',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Invariant Labs',
    author_email='security@invariantlabs.ai',
    py_modules=['simple_integer'],
    entry_points={
        'console_scripts': [
            'simple-integer-hello=simple_integer:post_install_message',
        ],
    },
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)