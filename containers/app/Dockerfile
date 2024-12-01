FROM python:latest

WORKDIR /app
COPY . /app

ENV FLASK_APP=main

# requirements.txtで指定された必要なパッケージをインストール
RUN pip install flask 
RUN pip install yfinance
RUN pip install -q -U google-generativeai
RUN pip install pymysql
RUN pip install cryptography 
RUN pip install flask-login

# ポートの公開
EXPOSE 5000