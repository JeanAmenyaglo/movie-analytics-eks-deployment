FROM python:3.11

# Set working directory
WORKDIR /workspace

# Copy requirements first
COPY requirements.txt .

# Install dependencies (Jupyter + pandas + matplotlib + etc.)
RUN pip install --no-cache-dir -r requirements.txt

# Copy notebook and dataset
COPY . .

# Expose JupyterLab port
EXPOSE 8888

# Start JupyterLab
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]