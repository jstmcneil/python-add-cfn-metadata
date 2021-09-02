FROM python:3

RUN pip3 install pyyaml

RUN mkdir scripts
COPY add_data.py /scripts/add_data.py
RUN chmod -R 777 scripts

ENTRYPOINT ["python3", "/scripts/add_data.py"]
