FROM python:slim
COPY app /app
RUN pip install flask
WORKDIR /app
ENTRYPOINT ["python3"]
CMD ["app2.py"]
