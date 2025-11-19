# EzShiksha – Smart Learning Platform

[![Live Demo](https://img.shields.io/badge/Demo-Live-success)](https://github.com/TilakRathoure/EzShiksha) [![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://ez-shiksha.vercel.app/)

**Simplify academics with AI-powered learning tools.** EzShiksha streamlines your study workflow by solving complex math problems, extracting text from images, and generating concise note summaries—all in one intelligent platform.

---

## 🚀 Features

- **🧮 Mathematical Problem Solver** – Solve complex equations instantly using SymPy
- **📸 OCR Text Extraction** – Extract text from images with Tesseract/EasyOCR
- **📝 Note Summarization** – Generate concise summaries from lengthy notes using fine-tuned T5-small model
- **✍️ Grammar & Spell Check** – AI-powered text correction and enhancement
- **🔐 Secure Authentication** – JWT-based user authentication and session management
- **🐳 Dockerized Deployment** – Containerized architecture for consistent environments
- **☁️ Cloud Deployment** – Frontend on Vercel, Backend on Render with FastAPI microservices

---

## 🛠️ Tech Stack

### Frontend
- **React.js** with TypeScript
- Deployed on **Vercel**

### Backend
- **Node.js** with Express
- **Python** with FastAPI (microservices)
- **MongoDB** for database
- Deployed on **Render** (Docker)

### AI/ML
- **SymPy** – Mathematical computation
- **Tesseract OCR / EasyOCR** – Optical Character Recognition
- **T5-small** – Fine-tuned on 2,000 custom notes for summarization
- **NLP** – Natural Language Processing for grammar correction

### DevOps
- **Docker** – Containerization
- **JWT** – Authentication & authorization

---

## 📸 Screenshots

<img width="950" height="639" alt="Dashboard Overview" src="https://github.com/user-attachments/assets/99894e68-5978-4952-bd1e-a6bdb80c1f0a" />

![Math Solver Interface](https://github.com/user-attachments/assets/525b45c5-6377-4092-9864-d8a4cc793902)

![OCR Text Extraction](https://github.com/user-attachments/assets/d01976be-046c-4366-ba6e-68cf6440d14a)

---

## 🏗️ Architecture

```
┌─────────────┐      ┌──────────────┐      ┌─────────────┐
│   Frontend  │─────▶│   Node.js    │─────▶│   MongoDB   │
│  (Vercel)   │      │   Backend    │      │  Database   │
└─────────────┘      │  (Render)    │      └─────────────┘
                     └──────┬───────┘
                            │
                     ┌──────▼───────┐
                     │   FastAPI    │
                     │ Microservice │
                     └──────────────┘
```

---

## 🔧 Environment Configuration

### Frontend (.env)
```env
REACT_APP_BACKEND_URL=http://localhost:5000
```

### Backend (.env)
```env
FRONTEND_URL=http://localhost:3000
JWT_SECRET=your_jwt_secret_here
MONGO_URL=mongodb://localhost:27017/
PORT=5000
FASTAPI=https://ezshiksha-fast-api.onrender.com
```

---

## 🐳 Docker Configuration

### Dockerfile
```dockerfile
FROM node:20-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3 python3-pip tesseract-ocr libtesseract-dev \
 && apt-get clean && rm -rf /var/lib/apt/lists/*

ENV PYTHONUNBUFFERED=1
ENV NODE_ENV=production

WORKDIR /app

# Install Node dependencies
COPY package*.json ./
RUN npm install --omit=dev

# Install Python dependencies
COPY requirements.txt ./
RUN pip3 install --break-system-packages --no-cache-dir -r requirements.txt \
 && pip3 install --break-system-packages --no-cache-dir sentencepiece

# Download and cache T5-small model
RUN python3 -c "from transformers import T5ForConditionalGeneration, T5Tokenizer; \
T5Tokenizer.from_pretrained('t5-small', cache_dir='/app/models'); \
T5ForConditionalGeneration.from_pretrained('t5-small', cache_dir='/app/models')"

ENV TRANSFORMERS_CACHE=/app/models

# Copy application code
COPY . .

EXPOSE 5000

CMD ["node", "server.js"]
```

---

## 🎯 Key Highlights

✨ **AI-Powered Learning** – Developed intelligent tools for solving mathematical equations, performing OCR-based text extraction, and generating concise note summarizations to enhance learning outcomes

🐳 **Containerized Architecture** – Dockerized the application and Tesseract OCR for consistent environments and seamless deployment across platforms

🤖 **Custom NLP Model** – Built and fine-tuned a T5-small model trained on 2,000 custom notes for grammar correction and high-quality note summarization

🔒 **Secure & Scalable** – Implemented JWT-based authentication with MongoDB for secure user management and scalable data storage

---

## 📦 Installation

### Prerequisites
- Node.js 20+
- Python 3.8+
- MongoDB
- Docker (optional)

### Local Development

1. **Clone the repository**
```bash
git clone YOUR_GITHUB_LINK
cd ezshiksha
```

2. **Install Frontend Dependencies**
```bash
cd frontend
npm install
```

3. **Install Backend Dependencies**
```bash
cd backend
npm install
pip3 install -r requirements.txt
```

4. **Configure Environment Variables**
- Create `.env` files in both frontend and backend directories
- Add the configurations mentioned above

5. **Run the Application**
```bash
# Frontend
npm start

# Backend
node server.js
```

### Docker Deployment
```bash
docker build -t ezshiksha .
docker run -p 5000:5000 ezshiksha
```
