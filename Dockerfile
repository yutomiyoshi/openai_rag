FROM python:3.10.0

WORKDIR /workspace

COPY ./app/requirements.txt .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

CMD ["tail", "-f", "/dev/null"]