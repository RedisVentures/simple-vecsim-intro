FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

EXPOSE 8501

RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install --upgrade pip setuptools wheel

COPY ./requirements.txt .

RUN pip3 install -r requirements.txt

WORKDIR /usr/src/app
COPY ./utils ./utils
COPY streamlit_app.py .


CMD streamlit run streamlit_app.py --server.port=8501 --server.address=0.0.0.0