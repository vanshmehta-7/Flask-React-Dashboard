# syntax=docker/dockerfile:1.4
FROM ubuntu:22.04

# Install OS-level packages
RUN export DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get --yes upgrade && \
    apt-get --yes install --no-install-recommends \
    python3.10-full tini build-essential

# Create and activate virtual environment
ENV VIRTUAL_ENV="/root/.venv"
RUN python3.10 -m venv "$VIRTUAL_ENV"
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Update pip
RUN pip install --upgrade pip setuptools wheel

# Setup root home directory
WORKDIR /backend

# Install package
COPY . .
RUN pip install -r requirements.txt

# Expose port 5000 for Flask app
EXPOSE 5000

ENTRYPOINT ["tini", "-v", "--"]
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]