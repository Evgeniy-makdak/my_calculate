FROM python:3.10
WORKDIR ./worker
RUN pip install redis
COPY . .
CMD ["python","./worker.py"]