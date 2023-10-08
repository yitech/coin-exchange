# Generate pb2 and pb2_grpc
```commandline
python -m grpc_tools.protoc --python_out=../exhost/ --grpc_python_out=../exhost/ -I. exhost.proto
```