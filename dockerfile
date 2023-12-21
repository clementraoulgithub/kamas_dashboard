FROM python:3.12.0b2
WORKDIR /app
COPY . /app/

RUN apt-get update \
    && apt-get -y install gcc mono-mcs \
    && rm -rf /var/lib/apt/lists/* \
    && python3 -m pip install --upgrade pip \
    && pip install -r requirements.txt

ENTRYPOINT [ "python", "-m", "gunicorn", "src.__main__:server", "-b", ":80"]
