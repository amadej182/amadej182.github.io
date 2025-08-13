FROM python:3.11-slim

WORKDIR /app

# Update package lists and install security updates
RUN apt-get update && apt-get upgrade -y && apt-get clean

RUN pip install --no-cache-dir django

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]