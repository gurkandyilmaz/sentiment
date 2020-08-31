FROM ubuntu:18.04

RUN apt-get update -y
RUN apt-get install -y python3 && apt-get install -y python3-pip
RUN pip3 install --upgrade pip

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app


RUN pip3 install -r requirements.txt

COPY . /app

#ENTRYPOINT export LC_ALL=C.UTF-8 export LANG=C.UTF-8 
#ENTRYPOINT export FLASK_APP=/app/flask_sentiment/app.py flask run 
 

ENTRYPOINT ["python3"]
CMD ["/app/flask_sentiment/app.py"]

