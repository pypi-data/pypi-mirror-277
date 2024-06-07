from setuptools import setup, find_packages

# Changelog information
changelog = """
Changelog:
0.1.6:
- Added support for TriangularWave.
- Improved efficiency of simulation routines.
0.1.5:
- Fixed bugs in the UART transmission logic.
0.1.4:
- Added Ramp and BandLimitedWhiteNoise waveforms.
"""

setup(
    name='pyblksim',
    version='0.1.7',
    packages=find_packages(),
    description='An Open-Source Model Based Simulator for Discrete-Time Simulations',
    long_description=changelog,  # Include changelog in the long description
    author='Dr. Kurian Polachan',
    author_email='kurian.polachan@iiitb.ac.in',
    license='GPLv3',
    install_requires=[
        'numpy',
        'matplotlib',
        'simpy',
        'scipy',
    ],
    python_requires='>=3.6',
    url='https://sites.google.com/view/cdwl/professor',
)
