FROM python:3.13-slim

# Create non-privileged user
RUN useradd -m appuser

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy only application package
COPY dominus-status dominus-status

# Give permissions to working directory
RUN chown -R appuser:appuser /app

USER appuser

EXPOSE 8000

CMD ["uvicorn", "dominus-status.main:app", "--host", "0.0.0.0", "--port", "8000"] 