FROM python:3.11-slim

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    chromium \
    chromium-driver \
    wget \
    unzip \
    libnss3 \
    libxss1 \
    libasound2 \
    libglib2.0-0 \
    libfontconfig1 \
    libgbm1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

ENV HEADLESS=true

VOLUME /app/reports
VOLUME /app/screenshots

CMD ["behave", "-f", "html", "-o", "reports/test_report.html"]