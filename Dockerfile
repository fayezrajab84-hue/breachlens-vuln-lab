# DELIBERATELY VULNERABLE — BreachLens container/IaC test target. Do NOT build+run.
# IaC: floating "latest" base tag, no non-root USER (runs as root), no HEALTHCHECK.
FROM python:latest

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

# No USER directive → the container runs as root.
CMD ["python", "app.py"]
