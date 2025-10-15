# Use official Node.js LTS image as base
FROM node:20-slim

# Install Python and other dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-pip tesseract-ocr libtesseract-dev git curl && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy Node.js project files
COPY package*.json ./
RUN npm install

# Copy Python requirements
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of your project
COPY . .

# Expose port (your Express app port)
EXPOSE 5000

# Start the Node.js server
CMD ["node", "index.js"]
