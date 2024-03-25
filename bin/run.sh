#!/bin/bash

docker run -d --name polyglot-container -v $(pwd)/app:/code/app -p 80:80 polyglot
