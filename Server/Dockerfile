FROM node:20-slim

# Install only necessary system dependencies
RUN apt-get update && apt-get install -y \
    python3 python3-pip tesseract-ocr libtesseract-dev \
 && apt-get clean && rm -rf /var/lib/apt/lists/*

ENV PYTHONUNBUFFERED=1
ENV NODE_ENV=production

WORKDIR /app

# Copy and install Node dependencies
COPY package*.json ./
RUN npm install

# Copy Python requirements and install
COPY requirements.txt .
RUN pip3 install --break-system-packages --no-cache-dir -r requirements.txt

# Copy rest of the app
COPY . .

EXPOSE 5000

CMD ["node", "server.js"]