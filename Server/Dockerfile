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

# Download model during build
RUN python3 -c "from transformers import T5ForConditionalGeneration, T5Tokenizer; \
T5Tokenizer.from_pretrained('t5-small', cache_dir='/app/models'); \
T5ForConditionalGeneration.from_pretrained('t5-small', cache_dir='/app/models')"
ENV TRANSFORMERS_CACHE=/app/models

# Copy rest of the app
COPY . .

EXPOSE 5000

CMD ["node", "server.js"]