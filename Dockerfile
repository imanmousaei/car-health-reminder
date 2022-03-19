FROM python:3

ADD . /car-health-reminder
WORKDIR /car-health-reminder

RUN pip install -r requirements.txt

CMD ["python", "main.py" ]
