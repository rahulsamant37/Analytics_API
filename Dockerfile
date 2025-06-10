# Use Python 3.12 slim image
FROM python:3.12-slim-bullseye

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

# Create a virtual environment using uv
RUN uv venv /opt/venv

# Set the virtual environment as the current location
ENV PATH=/opt/venv/bin:$PATH

# Set Python-related environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install os dependencies for our mini vm
RUN apt-get update && apt-get install -y \
    # for postgres
    libpq-dev \
    # for Pillow
    libjpeg-dev \
    # for CairoSVG
    libcairo2 \
    # other
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /code

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies using uv
RUN uv sync --frozen --no-cache

# Copy the project code
COPY ./src ./src


# make the bash script executable
COPY ./boot/docker-run.sh /opt/run.sh
RUN chmod +x /opt/run.sh

# Clean up apt cache to reduce image size
RUN apt-get remove --purge -y gcc \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Run the FastAPI project via the runtime script
# when the container starts
CMD ["/opt/run.sh"]