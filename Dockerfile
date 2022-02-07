FROM python:3.9-bullseye
COPY ./wbsrv.py . 
CMD python3 wbsrv.py
