# [🙊] Secret Spot | WMS tiles renderer

Renderer of `[🙊] Secret Spot` objects to WMS raster tiles using `Mapnik`.
Uses `PostgreSQL` database as a datasource.

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
