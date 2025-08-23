set -e  # Exit on any error

echo "Starting Render build process..."

# Install system packages needed for pytesseract & OpenCV
echo "Installing system dependencies..."
apt-get update && apt-get install -y tesseract-ocr libtesseract-dev

# Install Node.js dependencies
echo "Installing Node.js dependencies..."
npm install

# Install Python dependencies
echo "Installing Python dependencies..."
pip3 install -r requirements.txt

echo "Build completed successfully!"
