FROM python:3.4-alpine

RUN apk add bash && \
    pip install selenium pytest pytest-html