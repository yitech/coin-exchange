import grpc
import exhost.exhost_pb2 as exhost_pb2
import exhost.exhost_pb2_grpc as exhost_pb2_grpc

class gRPCClient:
    def __init__(self, host, port, logger):
        self.logger = logger

        self.channel = grpc.insecure_channel(f"{host}:{port}")
        self.stub = exhost_pb2_grpc.ExchangeStub(self.channel)

    def send_market_order(self, base, quote, side, qty, dry_run):
        request = exhost_pb2.MarketOrderRequest(
            base=base,
            quote=quote,
            side=side,
            qty=qty,
            dry_run=dry_run
        )

        response = self.stub.SendMarketOrder(request)
        res_id = next(response).id
        return res_id