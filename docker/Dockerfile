FROM python:alpine3.15

WORKDIR /usr/src/app

RUN apk --no-cache add musl-dev linux-headers g++
RUN python -m pip install --upgrade pip

COPY requirements.txt ./
RUN pip install -r requirements.txt


COPY . .

CMD [ "python", "./main.py" ]