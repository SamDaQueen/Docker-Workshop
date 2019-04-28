from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Flask Dockerised'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')



'''
katacoda docker - for practice
in docker file:
only one entry point/ multiple entry points
from - the os
run - install python/pip, dependencies, libraries
copy/workdir - the directory where app.py, requirements.txt are stored
expose - the port
entrypoint - python/ javac
cmd - the commands to run / file name to run
'''

'''
sudo apt install docker.io
sudo service docker start
sudo docker pull hello-world #pulls image
sudo docker run 
sudo docker ps -a #lists all images

for custom docker: 
to build:
sudo docker build -t flask-sample-one:latest . 
to make tag/give new name:
sudo docker tag flask-sample-one:latest new:v1
to run:
sudo docker run -d -p 80:5000 new:v1 #-d = detatched/background -p = ports
docker run -d --name redisMapped -v /opt/docker/data/redis:/data redis  #--name for custom name
to see output:
curl localhost:80
to stop:
sudo docker stop container_id
to start:
sudo docker start container_id
'''

'''
deleting containders and images:
sudo docker rm $(sudo docker ps -aq) -f
sudo docker rmi $(sudo docker images -aq) -f
'''














