FROM python:3-alpine

RUN apk add ffmpeg openssl

RUN pip install -U "yt-dlp[default]" "fastapi[standard]" "uvicorn[standard]" "cryptography"

WORKDIR /app

RUN openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365 -subj "/CN=localhost"

COPY *.py .

EXPOSE 8080

CMD ["fastapi", "run", "./server.py", "--port", "8080"]
#CMD ["tail", "-f", "/dev/null"]