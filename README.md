# Generate pb2 and pb2_grpc
```commandline
python -m grpc_tools.protoc --python_out=../exhost/ --grpc_python_out=../exhost/ -I. exhost.proto
```

# Docker build and push to DockerHub
```commandline
docker build -t automatons:latest .
docker tag automatons:latest yitech/automatons:latest
docker push yitech/automatons:latest
```
