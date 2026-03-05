FROM python:3.11-slim

WORKDIR app/

COPY app/ .

RUN pip install -r requirements.txt

COPY . .

CMD ["streamlit", "run", "app.py"]