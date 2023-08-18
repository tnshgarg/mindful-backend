FROM python:3.11
WORKDIR /code
COPY ./requirements.txt /code/
RUN pip install -r requirements.txt
# Copy the entire project
COPY ./ /code/
