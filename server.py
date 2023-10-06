import uuid
import logging
import grpc
from concurrent import futures
import exhost_pb2 as exhost_pb2
import exhost_pb2_grpc as exhost_pb2_grpc
from general.logger import LoggerConfig
from general.exchange import ExchangeFactory
from config.configuration import (
    LOG_DIR, EXCHANGE, TIMESTAMP, API, RPC_PORT
)


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



def serve():
    logger = LoggerConfig.setup_logger(LOG_DIR, EXCHANGE, 'exhost', TIMESTAMP, level=logging.DEBUG)
    exchange_handler = ExchangeFactory.get_handler(EXCHANGE, *API.values(), logger=logger)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    exhost_pb2_grpc.add_ExchangeServicer_to_server(ExchangeServicer(exchange_handler, logger), server)
    server.add_insecure_port(f'[::]:{RPC_PORT}')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()