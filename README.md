# Generate pb2 and pb2_grpc
```commandline
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. exhost.proto
```