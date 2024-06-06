from setuptools import setup, find_packages

# Read the requirements.txt file
with open("requirements.txt", encoding="utf-16-le") as f:
    requirements = f.read().splitlines()

# Remove BOM if present
if requirements[0].startswith('\ufeff'):
    requirements[0] = requirements[0][1:]

setup(
    name='zftracker',
    version='0.0.6',
    author='Junhao An',
    author_email='anjunhao_23@163.com',
    description='Python library for tracking group of zebrafish',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/zftracker',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Science/Research',
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires='>=3.9',
    install_requires=requirements,
)