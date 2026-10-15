# Base image pinned by digest (linux/amd64), not by tag: the pipeline builds
# amd64 only, so the digest is the same thing a tag pull would resolve to.
FROM python:3.12-slim@sha256:2b4f19dae3a777dfc3b76730bda1e82e1f66ab2a2686fa93ca78edbfb4f04ffe

LABEL org.opencontainers.image.title="mycom-app" \
      org.opencontainers.image.description="Lab package exercised by a build and publish pipeline"

WORKDIR /app

COPY pyproject.toml README.md ./
COPY src ./src

RUN pip install --no-cache-dir --no-compile .

# Run unprivileged: the image only needs to print a greeting.
USER 65532:65532

ENTRYPOINT ["mycom-app"]
CMD ["greet"]
