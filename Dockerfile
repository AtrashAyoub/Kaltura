FROM python:3.9
COPY requirements.txt ./
RUN pip3.9 install -r requirements.txt
COPY Parser.py .
EXPOSE 5000
CMD ["python", "./Parser.py"]