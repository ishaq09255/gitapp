# pull base image
FROM python:3-bullseye

#copy main code file
COPY run.py run.py

#copy dependencies

COPY requirements.txt requirements.txt


RUN pip install -r requirements.txt

ENTRYPOINT ["python", "run.py"]