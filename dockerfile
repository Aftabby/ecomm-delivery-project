# Use an official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy only the requirements file first
COPY requirements.txt .

# Install dependencies from requirements.txt
#RUN pip install --no-cache-dir -r requirements.txt     #No Cache
RUN pip install -r requirements.txt    #With Cache


# Copy the rest of the project files into the container
COPY . .

# Set default command
CMD ["python"]
#CMD ["bash"] 

#% For Using Flask directly from DOCKERFILE (Recommended for deployment)
#EXPOSE 5000
#CMD ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app"]

