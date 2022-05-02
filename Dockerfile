# base image
FROM python:3

#maintainer
MAINTAINER Anxhina  Gjoni
# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONBUFFERED 1

#directory to store app source code
RUN mkdir /musical

#switch to /app directory so that everything runs from here
WORKDIR /musical

#copy the app code to image working directory
COPY requirements.txt /musical/

#let pip install required packages
RUN pip install -r requirements.txt