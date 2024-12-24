FROM python:3.12

WORKDIR /app
COPY . /app

RUN pip install streamlit tensorflow pillow

EXPOSE 8501

CMD ["streamlit", "run", "animal_classifier_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
