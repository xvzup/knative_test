# Installation

* helm upgrade --install nats nats/nats -n nats --create-namespace -f nats-values.yaml --wait

## Reader

* kubectl run -it reader --image python:3.7-slim -- bash