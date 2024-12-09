FROM python:3-alpine

RUN apk add ffmpeg

RUN pip install -U "yt-dlp[default]" "fastapi[standard]"

WORKDIR /app

COPY *.py .

EXPOSE 8080

CMD ["fastapi", "run", "./server.py", "--port", "8080"]