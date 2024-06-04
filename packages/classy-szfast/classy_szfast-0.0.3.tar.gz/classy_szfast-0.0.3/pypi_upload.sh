#!/bin/bash

# Ensure to manually update the version number in setup.py before running this script

# Remove old build files
rm -rf build dist *.egg-info

# Build the package
python setup.py sdist bdist_wheel

# Upload the package
twine upload dist/*

# Clean up build directories
rm -rf build dist *.egg-info