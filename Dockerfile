FROM python:3.7
sdfsf dfsdf sdfsfd
EXPOSE 8501

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT [ "streamlit" ]
CMD [ "run", "src/main.py"]
