FROM node:20-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3 python3-pip tesseract-ocr libtesseract-dev git curl unzip openjdk-17-jdk-headless wget \
 && apt-get clean && rm -rf /var/lib/apt/lists/*

ENV PYTHONUNBUFFERED=1
ENV NODE_ENV=production
ENV LT_DIR=/usr/share/languagetool

WORKDIR /app

# Copy Node dependencies
COPY package*.json ./
RUN npm install

# Copy Python requirements
COPY requirements.txt .

# Ensure pip is up to date and clean install Python deps
RUN pip3 install --no-cache-dir --upgrade pip setuptools wheel \
 && pip3 install --break-system-packages --no-cache-dir -r requirements.txt --prefer-binary

# Pre-download LanguageTool
RUN mkdir -p /usr/share/languagetool && \
    curl -L -o /tmp/LanguageTool.zip https://languagetool.org/download/LanguageTool-stable.zip && \
    unzip /tmp/LanguageTool.zip -d /usr/share/languagetool && \
    mv /usr/share/languagetool/LanguageTool-* /usr/share/languagetool/LanguageTool-stable && \
    rm /tmp/LanguageTool.zip

# Copy the rest of the app
COPY . .

EXPOSE 5000

CMD ["node", "server.js"]
