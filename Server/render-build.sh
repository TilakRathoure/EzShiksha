set -e  # Exit on any error

echo "Starting Render build process..."

# Update apt and install tesseract OCR engine
echo "Installing system dependencies (Tesseract)..."
apt-get update && apt-get install -y tesseract-ocr python3-pip

# Install Node.js dependencies
echo "Installing Node.js dependencies..."
npm install

# Install Python dependencies
echo "Installing Python dependencies..."
pip3 install -r requirements.txt

echo "✅ Build completed successfully!"
