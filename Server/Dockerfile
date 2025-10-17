# Base image
FROM node:20-slim

# Install Python and Tesseract dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-pip tesseract-ocr libtesseract-dev git curl && \
    apt-get clean && rm -rf /var/lib/apt/lists/*
    
    
# Install Java
RUN apt-get update && apt-get install -y openjdk-17-jdk-headless wget

# LanguageTool Prebuild
RUN python3 -c "import language_tool_python; language_tool_python.LanguageTool('en-US')"


# Set working directory
WORKDIR /app

# Copy Node.js dependencies
COPY package*.json ./
RUN npm install
RUN npm install bcryptjs

# Copy Python requirements
COPY requirements.txt ./

# Install Python packages (break system packages allowed)
RUN pip3 install --break-system-packages --no-cache-dir -r requirements.txt

# Copy rest of the app
COPY . .

# Expose Express port
EXPOSE 5000

# Start Node.js server
CMD ["node", "server.js"]