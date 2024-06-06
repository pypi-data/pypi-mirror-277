from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r', encoding="UTF-8") as f:
        return f.read()


setup(
    name='Bybit_parser',
    version='0.0.3',
    author='db.boy',
    author_email='minkin.d.d@gmail.com',
    description='Данная библиотека предназначена для более удобной работы с api bybit',
    long_description=readme(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=[
        'requests',
        'pandas',
        'numpy',
        'tzlocal'
    ],
    classifiers=[
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    keywords='files speedfiles ',
    url="https://github.com/boyfws",
    python_requires='>=3.5'
)
