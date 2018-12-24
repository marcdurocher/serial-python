FROM python:3.6.7-alpine3.8

MAINTAINER Marc Durocher

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python -m modele.generatebin /mnt/function.bin

EXPOSE 8080

CMD ["python", "-m", "modele.endpoint","--file","/mnt/function.bin"]
