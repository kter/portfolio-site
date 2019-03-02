#!/bin/sh

/app/dart-sass/sass /app/main.scss /app/main.css
# aws s3 cp /app/main.css s3://$BUCKET_NAME