#!/bin/bash

docker build -t $AWS_ACCOUNT_ID.dkr.ecr.ap-southeast-1.amazonaws.com/polyglot:$(git rev-parse --short HEAD) . -f Dockerfile.production

docker push $AWS_ACCOUNT_ID.dkr.ecr.ap-southeast-1.amazonaws.com/polyglot:$(git rev-parse --short HEAD)
