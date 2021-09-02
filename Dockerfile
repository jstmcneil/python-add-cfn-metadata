FROM python:3

RUN pip3 install pyyaml

COPY add_data.py /add_data.py
RUN chmod 777 /add_data.py

ENTRYPOINT ["python3", "./add_data.py"]