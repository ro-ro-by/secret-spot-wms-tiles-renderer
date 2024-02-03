# Secret Spot WMS tiles renderer

Renderer of `SecretSpot` objects to WMS tiles using `Mapnik`

## Usage
```bash
docker run --rm -it -t \
  -v $(pwd)/tiles:/usr/src/renderer/tiles/ \
  --network {DB_NETWORK} \
  isxam/secret-spot-wms-tiles-renderer:latest python render.py 1 10 ./tiles/
```

## Docker Image

### Build
```bash
docker buildx build . --tag isxam/secret-spot-wms-tiles-renderer:latest
```

### Push
```bash
docker push isxam/secret-spot-wms-tiles-renderer:latest
```