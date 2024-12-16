FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install Flask
EXPOSE 80
CMD ["python", "app.py"]