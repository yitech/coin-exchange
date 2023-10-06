import grpc
import exhost_grpc.exhost_pb2 as exhost_pb2
import exhost_grpc.exhost_pb2_grpc as exhost_pb2_grpc
from config.configuration import RPC_HOST, RPC_PORT


def make_marker_order(base, quote, qty, side, dry_run):
    return exhost_pb2.MarketOrderRequest(base=base, quote=quote, qty=qty, side=side, dry_run=dry_run)


channel = grpc.insecure_channel(f'{RPC_HOST}:{RPC_PORT}')
client = exhost_pb2_grpc.ExchangeStub(channel)

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = exhost_pb2_grpc.ExchangeStub(channel)

    empty_request = exhost_pb2.Empty()
    result = stub.Sleep(empty_request)
    response = next(result)
    print(f"Received: {response.id}")

    # Send Market Order
    market_order = exhost_pb2.MarketOrderRequest(base="LTC", quote="USDT", qty=1.0, side="BUY", dry_run=False)
    result = stub.SendMarketOrder(market_order)
    response = next(result)
    print(f"Market Order Response: {response.id}")



if __name__ == '__main__':
    run()