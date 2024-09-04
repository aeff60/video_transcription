# ใช้ Python base image
FROM python

# ตั้งค่าตัวแปร ENV เพื่อให้ pip ทำงานแบบไม่ cache
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ติดตั้ง system dependencies ที่จำเป็น
RUN apt-get update && apt-get install -y \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# กำหนด working directory
WORKDIR /app

# คัดลอก requirements.txt และติดตั้ง dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# คัดลอก source code ทั้งหมดไปที่ /app
COPY . /app

# กำหนดให้ Flask รันบน host 0.0.0.0 เพื่อให้สามารถเข้าถึงได้จากภายนอก container
ENV FLASK_APP=app.py

# รันแอปพลิเคชัน
CMD ["flask", "run", "--host=0.0.0.0"]
