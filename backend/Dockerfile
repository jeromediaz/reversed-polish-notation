# Official image from docker hup
FROM python:3.13-slim

# Set the working directory
WORKDIR /backend

COPY . .

RUN pip install .[test]

RUN pytest tests


# Expose the application port
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]