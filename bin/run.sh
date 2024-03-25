#!/bin/bash

docker run -d --name polyglot-container -v $(pwd)/app:/code/app -p 80:80 \
    -e AWS_ACCESS_KEY_ID=[AWS_ACCESS_KEY_ID] -e AWS_SECRET_ACCESS_KEY=[AWS_SECRET_ACCESS_KEY] polyglot
