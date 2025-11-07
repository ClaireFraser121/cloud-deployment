
# Dockerfile

# codebases/simple_server/Dockerfile
# ────────────────────────────────────────────────────────────────
# Small Python base image for faster pulls
FROM python:3.12-slim

# Set working directory inside the image
WORKDIR /app

# Install dependencies first (better layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy only what we need (app code)
COPY app.py .

# Document the container's internal port
EXPOSE 5002

# Start the app with Gunicorn (module:object is app:app)
#  -b 0.0.0.0:5002 binds on the container port your workflow maps
#  --workers 2 is fine for now
#  --timeout 60 avoids long requests getting killed too quickly
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:5002", "--workers", "2", "--timeout", "60"]




# ────────────────────────────────────────────────────────────────
# WHERE:   Your laptop (source). Copied to EC2 during deploy.
# WHAT:    Build instructions for the image that will run on EC2.
# WHY:     Reproducible environment for your app.
# ────────────────────────────────────────────────────────────────

# # Small Python base image for faster pulls
# FROM python:3.12-slim

# # Set working directory inside the image
# WORKDIR /app

# # Install dependencies first (better layer caching)
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the application code
# COPY . .

# # Document the container's internal port
# EXPOSE 5002

# # Start the app (the PORT is provided by env; default is 5002)
# CMD ["python", "app.py"]


#__________________________________________________________________
# # Imagine this file as a recipe for setting up a virtual computer.

# # Dockerfiles typically start with a 'base image'. There are loads of these
# # and you can find them at hub.docker.com.
# # We're going to use a base image for Python veresion 3.11
# FROM python:3.11

# # This base image contains essentially everything necessary for a 'virtual
# # computer'. It has a terminal, certain basic commands, and of course Python.

# # We'll need our app's files in the container in order to be able to run them!
# # We copy them in from the current directory to the folder `/app` in
# # our virtual computer. Reminder `.` means 'the current directory'
# COPY . /app

# # We set the working directory for commands from this point on
# WORKDIR /app

# # We run `pipenv install` to install our project's dependencies. Since we've
# # copied in our `Pipfile`, `pipenv` will use that to get a list of dependencies.
# # We include a couple of extra options suitable for deployment.
# RUN pip install -r requirements.txt

# # At this point we've set up our virtual computer, but we've not _yet_ run our
# # application. And we're not going to! We're just setting up the container
# # so that it's ready to do so when we tell it.

# # So we're going to tell Docker here that when we _do_ want to run it, this is
# # what it should run:
# CMD ["python", "app.py"]
