# mycom-app

Small, self-contained Python package used as the *source* side of a two-repository
release lab.

- The package itself does one harmless thing: a CLI with `greet` and `version`.
- It exists so that a separate pipeline repository has something real to build,
  test, version-stamp, containerise and publish.

## Layout

```
pyproject.toml          packaging metadata (the pipeline stamps `version`)
src/mycom_app/          the package
tests/                  pytest suite
Dockerfile              image used by the pipeline's container leg
```

## Local use

```bash
python -m pip install -e '.[test]'
pytest
mycom-app greet --name lab
mycom-app version
```

## Notes for the pipeline

- The version lives only in `pyproject.toml`. The pipeline rewrites that field
  before building; the package reads the installed distribution metadata, so the
  two can never disagree.
- Everything here is throwaway test code. Nothing in this repository is intended
  for real consumption.
