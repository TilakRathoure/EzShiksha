FROM node:20-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3 python3-pip tesseract-ocr libtesseract-dev git curl unzip openjdk-17-jdk-headless wget \
 && apt-get clean && rm -rf /var/lib/apt/lists/*

ENV PYTHONUNBUFFERED=1
ENV NODE_ENV=production
ENV LT_DIR=/usr/share/languagetool

WORKDIR /app

# Copy and install Node dependencies
COPY package*.json ./
RUN npm install

# Copy Python requirements and install
COPY requirements.txt .
RUN pip3 install --break-system-packages --no-cache-dir -r requirements.txt

# Pre-download LanguageTool
RUN mkdir -p /usr/share/languagetool && \
    wget https://languagetool.org/download/LanguageTool-stable.zip -O /tmp/languagetool.zip && \
    unzip /tmp/languagetool.zip -d /usr/share/languagetool && \
    rm /tmp/languagetool.zip

# Copy rest of the app
COPY . .

EXPOSE 5000

CMD ["node", "server.js"]
