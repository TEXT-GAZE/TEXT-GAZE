#!/bin/bash

# Update package lists
apt-get update

# Install Tesseract
apt-get install -y tesseract-ocr

# Install other dependencies
pip install -r requirements.txt
