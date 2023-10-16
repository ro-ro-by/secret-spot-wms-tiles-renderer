# Secret Spot WMS tiles renderer

Renderer of `SecretSpot` objects to WMS tiles using `Mapnik`

## Installation
```bash
docker build . --tag wms-tiles-renderer:latest
```

## Usage
```bash
docker run --rm -it -t \
  -v $(pwd)/tiles:/usr/src/renderer/tiles/ \
  --network {DB_NETWORK} \
  wms-tiles-renderer:latest python render.py 1 10 ./tiles/
```
