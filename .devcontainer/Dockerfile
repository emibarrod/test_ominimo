FROM mcr.microsoft.com/devcontainers/python:3.13-bullseye

USER vscode

# Install uv, dbt, and airflow
RUN pip install --upgrade pip && \
    pip install uv

# Install DuckDB in the user's home directory
RUN curl https://install.duckdb.org | sh

# Add DuckDB to the PATH
RUN echo 'export PATH="$HOME/.duckdb:$PATH"' >> /home/vscode/.bashrc

