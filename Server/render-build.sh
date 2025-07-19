#!/bin/bash
set -e  # Exit on any error

echo "Starting Render build process..."

# Install Node.js dependencies
echo "Installing Node.js dependencies..."
npm install

# Install Python dependencies
echo "Installing Python dependencies..."
pip3 install -r requirements.txt
cd ..

echo "Build completed successfully!"
