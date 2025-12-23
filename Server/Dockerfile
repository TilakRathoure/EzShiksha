FROM node:20-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3 python3-pip tesseract-ocr libtesseract-dev \
 && apt-get clean && rm -rf /var/lib/apt/lists/*

ENV PYTHONUNBUFFERED=1
ENV NODE_ENV=production

WORKDIR /app

# ---- Node dependencies ----
COPY Server/package*.json ./
RUN npm install --omit=dev

# ---- Python dependencies ----
COPY Server/requirements.txt ./
RUN pip3 install --break-system-packages --no-cache-dir -r requirements.txt \
 && pip3 install --break-system-packages --no-cache-dir sentencepiece

# ---- Download model at build time (heavy but intentional) ----
RUN python3 -c "from transformers import T5ForConditionalGeneration, T5Tokenizer; \
T5Tokenizer.from_pretrained('t5-small', cache_dir='/app/models'); \
T5ForConditionalGeneration.from_pretrained('t5-small', cache_dir='/app/models')"

ENV TRANSFORMERS_CACHE=/app/models

# ---- App source ----
COPY Server/. .

EXPOSE 5000

CMD ["node", "server.js"]
