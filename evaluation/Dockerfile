# Build a scorer image before registering the CodaBench task.
FROM python:3.12-slim
RUN apt-get update && apt-get install -y --no-install-recommends git && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir 'numpy>=2,<3' 'scikit-learn>=1.5,<2' && \
    pip install --no-cache-dir --no-deps 'git+https://github.com/OpenSportsLab/opensportslib.git@dc96cbfd0128fa77cb3bf1b3319e5fdf8c53b5a7'
COPY scoring.py /app/scoring.py
WORKDIR /app
CMD ["python", "scoring.py"]
