# Build stage
FROM python:3.11-slim-buster AS build

# Create a non-root user to run the app
RUN adduser --disabled-password --gecos '' user-admission
USER user-admission

# Set the working directory to /app
WORKDIR /app

# Copy only the requirements file to the container
COPY requirements.txt .

# Set the path variable
ENV PATH=/home/user-admission/.local/bin:$PATH

# Upgrade pip by python
RUN python -m pip install --upgrade pip

# Install requirements
RUN pip install --no-cache-dir --user -r requirements.txt

# Final stage
FROM python:3.11-slim-buster

# Create a non-root user to run the app
RUN adduser --disabled-password --gecos '' user-admission
USER user-admission

# Set the working directory to /app
WORKDIR /app

# Copy the app code from the build stage to the container
COPY --from=build /home/user-admission/.local /home/user-admission/.local

# Set environment variables
ENV PATH=/home/user-admission/.local/bin:$PATH \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    FLASK_APP=main.py \
    FLASK_ENV=development \
    SECRET_KEY=@admission-hub@

# Copy the rest of the app code to the container
COPY main.py .

# Set the default command to start the app
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
