#!/usr/bin/env bash

set -euxo pipefail

source="$1"
target="${2:$source}"
fullTarget="s3://${BUCKET}/${target}"

$HOME/.local/bin/aws s3 cp "${source}" "${fullTarget}"

