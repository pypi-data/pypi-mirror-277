from setuptools import setup, find_packages

setup(
    name='maithongpackage999',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.18.5',
        'pandas>=1.0.5',
        'requests>=2.23.0'
    ],
    author='Nutthavate',
    author_email='chaikaew902@gmail.com',
    description='ตัวอย่างการสร้าง Package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Pick999999/my_package',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
