# Installation

* helm upgrade --install nats nats/nats -n nats --create-namespace -f nats-values.yaml --wait

## Reader

* kubectl run -it reader --image python:3.7-slim -- bash

## Oauth2Proxy

* kubectl create secret generic oauth2-proxy-config --from-file=./K8s/oauth2_proxy.cfg
