FROM python:3.7

EXPOSE 8501
dnkajkjqwd qdwkjqwd
WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT [ "streamlit" ]
CMD [ "run", "src/main.py"]
