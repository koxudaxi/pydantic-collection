#!/usr/bin/env bash
set -e

black pydantic_collection tests --skip-string-normalization
isort --recursive -w 88  --combine-as --thirdparty pydantic_collection pydantic_collection tests -m 3 -tc
