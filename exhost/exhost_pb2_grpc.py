# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import exhost.exhost_pb2 as exhost__pb2


class ExchangeStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendMarketOrder = channel.unary_stream(
                '/exhost.Exchange/SendMarketOrder',
                request_serializer=exhost__pb2.MarketOrderRequest.SerializeToString,
                response_deserializer=exhost__pb2.Hash.FromString,
                )
        self.SendLimitOrder = channel.unary_stream(
                '/exhost.Exchange/SendLimitOrder',
                request_serializer=exhost__pb2.LimitOrderRequest.SerializeToString,
                response_deserializer=exhost__pb2.Hash.FromString,
                )


class ExchangeServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SendMarketOrder(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendLimitOrder(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ExchangeServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendMarketOrder': grpc.unary_stream_rpc_method_handler(
                    servicer.SendMarketOrder,
                    request_deserializer=exhost__pb2.MarketOrderRequest.FromString,
                    response_serializer=exhost__pb2.Hash.SerializeToString,
            ),
            'SendLimitOrder': grpc.unary_stream_rpc_method_handler(
                    servicer.SendLimitOrder,
                    request_deserializer=exhost__pb2.LimitOrderRequest.FromString,
                    response_serializer=exhost__pb2.Hash.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'exhost.Exchange', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Exchange(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SendMarketOrder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/exhost.Exchange/SendMarketOrder',
            exhost__pb2.MarketOrderRequest.SerializeToString,
            exhost__pb2.Hash.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendLimitOrder(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/exhost.Exchange/SendLimitOrder',
            exhost__pb2.LimitOrderRequest.SerializeToString,
            exhost__pb2.Hash.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
