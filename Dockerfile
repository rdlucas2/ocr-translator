FROM python:latest

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN apt-get update

RUN apt-get install zlib1g-dev python-dev libxml2-dev libxslt1-dev antiword unrtf poppler-utils tesseract-ocr flac ffmpeg lame libmad0 libsox-fmt-mp3 sox libjpeg-dev swig tesseract-ocr-rus -y

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./src/main.py /app/main.py

ENTRYPOINT [ "python", "/app/main.py" ]
