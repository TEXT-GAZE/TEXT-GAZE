# #!/bin/bash

# # Update package lists
# apt-get update

# # Install Tesseract
# apt-get install -y tesseract-ocr

# # Install other dependencies
# pip install -r requirements.txt



#!/bin/bash

# Stop the script if any command fails
set -e

# Update package lists
echo "Updating package lists..."
apt-get update

# Install Tesseract
echo "Installing Tesseract..."
apt-get install -y tesseract-ocr

# Install other dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Verify Tesseract installation
echo "Verifying Tesseract installation..."
tesseract --version

echo "Build completed successfully!"

