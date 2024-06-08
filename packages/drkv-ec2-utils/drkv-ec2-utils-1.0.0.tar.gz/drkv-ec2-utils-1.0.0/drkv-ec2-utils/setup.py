from setuptools import setup

setup(
    name='drkv-ec2-utils',
    version='1.0.0',
    author="drkv - Duesseldorf - Germany",
    author_email="m.kirchhof@drkv.com",
    description="Python module to onboard the EC2 Utills Library",
    packages=["drkv-ec2-utils"],
    install_requires=[
        "boto3 >= 1.34.48",
        "pycryptodome >= 3.20.0",
    ],
    classifiers=[
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',
)