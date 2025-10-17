# Base image
FROM node:20-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3 python3-pip tesseract-ocr libtesseract-dev git curl openjdk-17-jdk-headless wget \
 && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV NODE_ENV=production
ENV LT_CACHE_DIR=/usr/share/languagetool_cache

WORKDIR /app

# Copy Node.js dependencies and install
COPY package*.json ./
RUN npm install

# Copy Python requirements and install
COPY requirements.txt .
RUN pip3 install --break-system-packages --no-cache-dir -r requirements.txt

# Prebuild LanguageTool cache
RUN mkdir -p $LT_CACHE_DIR && \
    python3 - <<'PYCODE'
import os
import language_tool_python
tool = language_tool_python.LanguageTool('en-US', cache_dir=os.getenv("LT_CACHE_DIR"))
print("LanguageTool prebuilt successfully at:", os.getenv("LT_CACHE_DIR"))
PYCODE

# Copy the rest of the app
COPY . .

EXPOSE 5000

CMD ["node", "server.js"]
