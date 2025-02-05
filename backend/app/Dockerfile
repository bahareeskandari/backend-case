FROM python:3.9

WORKDIR /app

# copy the requirements in requirements.txt and start installing from that file
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt 

# copies all of our files in the app folder to the docker image
COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
