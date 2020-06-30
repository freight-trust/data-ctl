#!/bin/bash -e
# for entire folder, will generate sha256sum then *append* to a file, for different usage change &>> to w/e.
find . -type f -exec sha256sum {} \; &>> SHA256SUMS
