FROM ghcr.io/astral-sh/uv:python3.13-bookworm

WORKDIR /app

RUN curl -L -O https://raw.githubusercontent.com/vishnubob/wait-for-it/refs/heads/master/wait-for-it.sh && chmod +x wait-for-it.sh

COPY . .

RUN uv sync --frozen

EXPOSE 8000

