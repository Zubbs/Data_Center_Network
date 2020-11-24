FROM python:3.6-slim

RUN apt-get update && \
  apt-get install -qq -y \
  build-essential \
  netcat \
  libpq-dev \
  --no-install-recommends

WORKDIR /app

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
ENV FLASK_APP="/app/main.py"
ENV PYTHONDONTWRITEBYTECODE=1
CMD ["flask",  "run", "--host=0.0.0.0", "--port=5000"]
