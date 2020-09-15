# Assignment_project

A simple web application with a database which will perform two simple tasks -> GET / SET

# Getting started
Download Docker Desktop for Mac or Windows. Docker Compose will be automatically installed. 
https://hub.docker.com/editions/community/docker-ce-desktop-windows/

On Linux, make sure you have the latest version of Compose. https://docs.docker.com/compose/ 

# You are required to change your host file:
https://www.howtogeek.com/howto/27350/beginner-geek-how-to-edit-your-hosts-file/

Change the host file such that webapp.com is pointing to the docker host.
For example:

192.168.18.4 webapp.com

# How to run this application in your linux server
git clone https://github.com/tanboonheng/assignment_project.git

cd assignment_project

docker-compose up
