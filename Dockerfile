FROM python:3.10.0a4-alpine

RUN apk update && \
    apk add bash && \
    pip install selenium pytest pytest-html