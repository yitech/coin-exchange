import uuid
import grpc
import argparse
import logging.config
from concurrent import futures
import exhost.exhost_pb2 as exhost_pb2
import exhost.exhost_pb2_grpc as exhost_pb2_grpc
from general.utils import read_json
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


if __name__ == "__main__":
    logging.config.fileConfig('./config/logging_config.ini')
    logger = logging.getLogger("gRPC")

    parser = argparse.ArgumentParser(description='Start the gRPC server.')
    parser.add_argument('--config', default='./config/config.grpc.json', type=str, help='Path to the JSON config file.')
    args = parser.parse_args()

    config = read_json(args.config)
    logger.info(f"{config=}")

    server(config["port"], config["exchange"], logger, *config["api"])
