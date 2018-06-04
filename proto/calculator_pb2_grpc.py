# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from proto import calculator_pb2 as proto_dot_calculator__pb2


class CalculatorStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SquareRoot = channel.unary_unary(
        '/Calculator/SquareRoot',
        request_serializer=proto_dot_calculator__pb2.Number.SerializeToString,
        response_deserializer=proto_dot_calculator__pb2.Number.FromString,
        )
    self.ReceiveEvents = channel.unary_stream(
        '/Calculator/ReceiveEvents',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=proto_dot_calculator__pb2.Number.FromString,
        )
    self.SendEvents = channel.stream_unary(
        '/Calculator/SendEvents',
        request_serializer=proto_dot_calculator__pb2.Number.SerializeToString,
        response_deserializer=proto_dot_calculator__pb2.Number.FromString,
        )
    self.Chat = channel.stream_stream(
        '/Calculator/Chat',
        request_serializer=proto_dot_calculator__pb2.Number.SerializeToString,
        response_deserializer=proto_dot_calculator__pb2.Number.FromString,
        )


class CalculatorServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def SquareRoot(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReceiveEvents(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SendEvents(self, request_iterator, context):
    """Return the total count of event
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Chat(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CalculatorServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SquareRoot': grpc.unary_unary_rpc_method_handler(
          servicer.SquareRoot,
          request_deserializer=proto_dot_calculator__pb2.Number.FromString,
          response_serializer=proto_dot_calculator__pb2.Number.SerializeToString,
      ),
      'ReceiveEvents': grpc.unary_stream_rpc_method_handler(
          servicer.ReceiveEvents,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=proto_dot_calculator__pb2.Number.SerializeToString,
      ),
      'SendEvents': grpc.stream_unary_rpc_method_handler(
          servicer.SendEvents,
          request_deserializer=proto_dot_calculator__pb2.Number.FromString,
          response_serializer=proto_dot_calculator__pb2.Number.SerializeToString,
      ),
      'Chat': grpc.stream_stream_rpc_method_handler(
          servicer.Chat,
          request_deserializer=proto_dot_calculator__pb2.Number.FromString,
          response_serializer=proto_dot_calculator__pb2.Number.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Calculator', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
