# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.9-alpine3.13

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
RUN /usr/local/bin/python -m pip install --upgrade pip
COPY requirements.txt /tmp/requirements.txt
RUN python -m pip install -r /tmp/requirements.txt && \
    rm -rf /tmp

WORKDIR /app
COPY /app /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app.wsgi"]
