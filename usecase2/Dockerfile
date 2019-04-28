FROM ubuntu:16.04
RUN apt-get clean 
RUN apt-get update -y 
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
EXPOSE 6000
ENTRYPOINT ["python"]
CMD ["u2.py"]
