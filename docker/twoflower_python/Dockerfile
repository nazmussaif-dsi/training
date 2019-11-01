FROM python:3.7.3-stretch
RUN apt update && apt install -y python3-flask
WORKDIR /usr/src/app
COPY python ./
ENV FLASK_ENV=development
ENV FLASK_APP=app.py
CMD [ "flask", "run", "--host=0.0.0.0","--port=8080"]
