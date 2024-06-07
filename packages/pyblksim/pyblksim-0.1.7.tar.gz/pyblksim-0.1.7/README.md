# PyBlkSim
An Open-Source Model Based Simulator for Discrete-Time Simulations

# Installation
### from github repository; once the repository is made public
$pip install "git+https://github.com/kurianpolachan-iiitb/pyblksim.git"
### from local clone of the github repository
$CD Local-Github-Project-Directory
$pip install .

# Uploading to PyPi
$python -m twine upload .\dist\* --verbose
The above command will ask for an API key. Get it from pypi and paste (it will not show the pasted code, dont worry go ahead and press enter)
Ensure that only the latest builds are in the .\dist\*
For every new upload, change the version of the module in the setup.py.

# Notes
1. Anytime the source is updated, remember to increment the version in setup.py
