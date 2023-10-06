import uuid
import grpc
from concurrent import futures
import exhost_pb2 as exhost_pb2
import exhost_pb2_grpc as exhost_pb2_grpc
from general.exchange import ExchangeFactory


class ExchangeServicer(exhost_pb2_grpc.ExchangeServicer):
    def __init__(self, exchange_handler, logger):
        self.exchange_handler = exchange_handler
        self.logger = logger

    def SendMarketOrder(self, request, context):
        unique_id = uuid.uuid4().hex
        self.logger.info(f"Request ID: {unique_id}")
        yield exhost_pb2.Hash(id=unique_id)
        self.logger.info(f'Send {request=}')
        res = self.exchange_handler.create_market_order(request.base, request.quote, request.side, request.qty,
                                                        request.dry_run)
        self.logger.info(f'Receive {res=}')

    def SendLimitOrder(self, request, context):
        # Not test yet
        unique_id = uuid.uuid4().hex
        self.logger.info(f"Request ID: {unique_id}")
        yield exhost_pb2.Hash(id=unique_id)


def server(port:int, exchange: str, logger, *api):
    exchange_handler = ExchangeFactory.get_handler(exchange, *api, logger=logger)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    exhost_pb2_grpc.add_ExchangeServicer_to_server(ExchangeServicer(exchange_handler, logger), server)
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    server.wait_for_termination()
