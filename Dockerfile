FROM python:3.8

RUN pip install pyspark
RUN apt-get update

RUN apt-get install default-jdk -y
RUN pip install numpy
WORKDIR /usr/src/app

COPY . .

RUN echo $(pwd)
CMD [ "python", "/usr/src/app/main.py" ]
