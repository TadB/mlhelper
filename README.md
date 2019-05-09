python version 3.7

install locally:  
```
pip install -r requirements.txt
export FLASK_APP="mlhelper.py"
flask db upgrade

```

run locally:\
`flask run`

docker:
```
docker run --name redis -d -p 6379:6379 redis:5-alpine
docker build -t mlhelper:latest . 
docker run --name mlhelper -d -p 8000:5000 --rm --link redis:redis-server -e REDIS_URL=redis://redis-server:6379/0 mlhelper:latest
docker run --name rq-worker -d --rm --link redis:redis-server -e REDIS_URL=redis://redis-server:6379/0 --entrypoint venv/bin/rq mlhelper:latest worker -u redis://redis-server:6379/0 mlhelper-tasks
```

## Decisions:
- Relational DATABASE 
	- using orm: flask-sqlalchemy to allow easily change database system in production environment
	- sqlite as a simple, file based database system for development
	- text from websites are stored in database
	- for images stored only paths to files, to save database storage
	- images stored in file system 
- Function to save images and text from website, search only in tags with class='post' tags. It allows the user to save content from site and skip navigation section, comments section etc.
- in add_images function while saving images, commit to database are made after all successfully saved images, to handle all images as one transaction.

# Description
In all routes, user need to specify url parameter and send it to server as a json in format:
`{"url": "website url adress"}`
All main functions return json response message. 
Function for downloading resources, return zip file with all stored images and text in .txt file for given website.

