FROM python:3.10.6-alpine
WORKDIR /backend
COPY . .
ENV PYTHONPATH "${PYTHONPATH}:/"
RUN pip install "poetry==1.5.1"
RUN poetry config virtualenvs.create false && poetry config installer.max-workers 10
RUN poetry install --no-root
CMD ["python", "main.py"]