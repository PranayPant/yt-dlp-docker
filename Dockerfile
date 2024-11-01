FROM python:3-alpine

RUN pip install -U "yt-dlp[default]" "fastapi[standard]"

WORKDIR /app

COPY *.py .

EXPOSE 80

CMD ["fastapi", "run", "./server.py", "--port", "80"]