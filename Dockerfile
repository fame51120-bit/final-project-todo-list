   # Stage 1: Builder
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Final - เล็กและปลอดภัย
FROM python:3.11-slim
WORKDIR /app
RUN useradd -m appuser
COPY --from=builder /root/.local /home/appuser/.local
COPY app.py security.html performance.html ./
COPY tasks.json* ./
RUN chown -R appuser:appuser /app
USER appuser
ENV PATH=/home/appuser/.local/bin:$PATH
EXPOSE 10000
CMD ["python", "app.py"]
