# Use the specified Python version
FROM python:3.8.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /code

# Copy the requirements file into the container
COPY ./src/requirements.txt /code/

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the source code into the container
COPY ./src /code/

# Command to run the Uvicorn server
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
