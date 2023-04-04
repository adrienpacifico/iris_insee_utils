FROM python
WORKDIR /app
COPY  . /app
RUN pwd
RUN ls
RUN pip install -r requirements.txt
RUN pip install -e .