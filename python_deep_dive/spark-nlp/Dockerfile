FROM ubuntu:18.04

WORKDIR /usr/src/app
RUN apt-get update
RUN apt-get install openjdk-8-jdk -y
RUN apt-get install wget -y
RUN apt-get install software-properties-common -y

RUN curl https://dlcdn.apache.org/spark/spark-3.3.0/spark-3.3.0-bin-hadoop2.tgz
RUN tar xf spark-3.3.0-bin-hadoop2.tgz

RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get install python3.9 -y
RUN apt-get install python3.9-dev -y
RUN apt install python3.9-distutils -y
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3.9 get-pip.py

COPY ./app /usr/src/app
RUN python3.9 -m pip install --upgrade setuptools
RUN python3.9 -m pip install --upgrade pip
RUN python3.9 -m pip install --upgrade distlib

RUN python3.9 -m pip install cython numpy
RUN python3.9 -m pip install cython numpy
RUN python3.9 -m pip install -r requirements.txt

ENV JAVA_HOME  "/usr/lib/jvm/java-8-openjdk-amd64"
ENV PATH=$SPARK_HOME/bin:$PATH

CMD ["python3.9", "run_forever.py"]
