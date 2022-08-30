# Smart applications in Python
Collection of completed tasks and project build at my university.
Tasks and their solutions are stored in notebooks in main directory and project in a separate directory - **PROJECT**.
Enjoy :muscle:

# Getting started
1. Clone this repo
```
git clone https://github.com/krzysztofhewelt/Smart-applications-Python
```
2. Build docker image from Dockerfile
```
docker build -t jupyter .
```
3. Run docker command to run Jupyter environment in container
**Windows users**
```
docker run -it --rm -p 8888:8888 -v "%cd%":/home/jovyan/work jupyter
```
**Linux users**
```
docker run -it --rm -p 8888:8888 -v "${PWD}":/home/jovyan/work jupyter
```
4. Open Jupyter in web browser on address
```
http://127.0.0.1:8888/lab?token=<GENRATED TOKEN>
```

# Technologies
- Python
- Apache Spark and MLlib
- Jupyter
- Docker
