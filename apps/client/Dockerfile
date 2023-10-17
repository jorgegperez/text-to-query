FROM python:3.9

RUN mkdir /client

COPY requirements.txt /client

WORKDIR /client

RUN pip install -r requirements.txt

COPY . /client

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]