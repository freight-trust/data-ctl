#!/bin/bash
# Sign a file with a private key using OpenSSL
# Encode the signature in Base64 format
#
# Usage: sign <file> <private_key>
#
# NOTE: to generate a public/private key use the following commands:
#
# openssl genrsa -aes128 -passout pass:<passphrase> -out private.pem 2048
# openssl rsa -in private.pem -passin pass:<passphrase> -pubout -out public.pem
#
# where <passphrase> is the passphrase to be used.
# from user @ezimuel via https://gist.github.com/ezimuel/3cb601853db6ebc4ee49
# 

${FILE}=filename
${PKEY}=${PRIV_KEY}

filename=$1
# privatekey=$2

if [[ $# -lt 2 ]] ; then
  echo "Usage: sign <file> <private_key>"
  exit 1
fi

openssl dgst -sha256 -sign ${PKEY} -out /tmp/$filename.sha256 ${FILE}
openssl base64 -in /tmp/$filename.sha256 -out signature.sha256
rm /tmp/$filename.sha256
