from setuptools import setup, find_packages
setup(
    name='hwo_custom_markers',
    version='1.0',
    author='Susan F. Redmond',
    description='Custom matplotlib markers for aperture concepts',
    long_description='',
    url='https://github.com/sfr348/hwo_custom_markers',
    keywords='development, setup, setuptools',
    python_requires='>=3.7, <4',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'hwo_custom_markers': ['support_data/*.svg'],
    },
    install_requires=[
        'numpy>=1.14.5',
        'matplotlib>=2.2.0',
        'jupyter',
        'svgpath2mpl',
        'svgpathtools'
    ],
)
