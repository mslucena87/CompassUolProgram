FROM python:latest
LABEL Maintainer="msoareslucena"
WORKDIR /usr/app/src
COPY main.py .
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install -r requirements.txt 
CMD [ "python", "./main.py" ]
