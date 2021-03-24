FROM python:3.8.8-alpine

RUN apk update && \
    apk add bash && \
    pip install selenium pytest pytest-html