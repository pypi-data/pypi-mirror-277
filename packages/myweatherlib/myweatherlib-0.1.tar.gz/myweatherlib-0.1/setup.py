from setuptools import setup, find_packages

setup(
    name='myweatherlib',
    version='0.1',
    author='Patryk',
    author_email='tryczek5@gmail.com',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
