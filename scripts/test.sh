#!/usr/bin/env bash
set -e

export AWS_DEFAULT_REGION=us-west-2
pytest --cov=pydantic_collection --cov-report=xml --cov-report=term-missing  tests