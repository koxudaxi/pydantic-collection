#!/usr/bin/env bash
set -e

black pydantic_collection tests --check --skip-string-normalization
isort --recursive --check-only -w 88  --combine-as --thirdparty pydantic_collection pydantic_collection tests -m 3 -tc
mypy pydantic_collection --disallow-untyped-defs --ignore-missing-imports