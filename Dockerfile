# Use an official lightweight Python image
FROM python:3.11-slim


# Set working directory
WORKDIR /app


# Copy requirements and install
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


# Copy app source
COPY . /app


# Expose port
ENV PORT=8080
EXPOSE ${PORT}


# Run the Flask app
CMD ["python", "app.py"]
