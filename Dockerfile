FROM python:alpine

COPY ./kasa-estream/main.py /app/estream/
WORKDIR /app/estream/
RUN pip install python-kasa

CMD ["python3", "main.py"]