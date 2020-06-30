#!/bin/bash -e
find . -type f -exec sha256sum {} \; &>> SHA256SUMS
