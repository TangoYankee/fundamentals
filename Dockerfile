FROM python:3.6

WORKDIR /app

ADD requirements.txt /app
ADD app.py /app
ADD wsgi.py /app

COPY . /app

RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app"]
