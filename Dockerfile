<<<<<<< HEAD
@"
=======
>>>>>>> aa8c7958e5cba90904bad6ac6612946e20ea33c4
FROM python:3.11-slim
WORKDIR /app
COPY inventory_manager.py .
CMD ["python", "inventory_manager.py"]
<<<<<<< HEAD
"@ | Set-Content -Encoding ascii Dockerfile
=======
>>>>>>> aa8c7958e5cba90904bad6ac6612946e20ea33c4
