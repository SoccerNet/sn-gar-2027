FROM python:3.12-slim
RUN apt-get update && apt-get install -y --no-install-recommends git && rm -rf /var/lib/apt/lists/*
COPY requirements-scoring.txt /app/requirements-scoring.txt
RUN pip install --no-cache-dir -r /app/requirements-scoring.txt && \
    pip install --no-cache-dir --no-deps 'git+https://github.com/OpenSportsLab/opensportslib.git@dc96cbfd0128fa77cb3bf1b3319e5fdf8c53b5a7'
COPY scoring.py /app/scoring.py
WORKDIR /app
CMD ["python", "scoring.py"]
