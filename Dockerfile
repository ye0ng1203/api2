FROM python:3

RUN mkdir /app
WORKDIR /app
COPY app1.py ./ 
COPY models1.py ./
COPY requirements.txt .
RUN pip3 install -r requirements.txt
CMD python app1.py
