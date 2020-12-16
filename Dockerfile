FROM python:3.6-slim

EXPOSE 5011

COPY ./app.py /app/app.py
COPY ./Pipfile* /app/

RUN pip install pipenv
RUN cd /app && pipenv lock --requirements > requirements.txt
RUN pip install -r /app/requirements.txt

CMD ["python", "/app/app.py"]
