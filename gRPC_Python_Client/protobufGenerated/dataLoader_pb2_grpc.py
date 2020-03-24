# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from protobufGenerated import dataLoader_pb2 as dataLoader__pb2


class DataLoaderStub(object):
  """Сервис, ответственный за передачу данных клиенту.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.FetchData = channel.unary_unary(
        '/BSU.DataLoader.DataLoader/FetchData',
        request_serializer=dataLoader__pb2.TaskDataRequest.SerializeToString,
        response_deserializer=dataLoader__pb2.TaskDataReply.FromString,
        )
    self.FetchDataAsStream = channel.unary_stream(
        '/BSU.DataLoader.DataLoader/FetchDataAsStream',
        request_serializer=dataLoader__pb2.TaskDataRequest.SerializeToString,
        response_deserializer=dataLoader__pb2.TaskDataReply.FromString,
        )


class DataLoaderServicer(object):
  """Сервис, ответственный за передачу данных клиенту.
  """

  def FetchData(self, request, context):
    """Возвращает данные целиком. Один запрос - один ответ.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FetchDataAsStream(self, request, context):
    """Сервер возвращает клиенту поток для чтения.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DataLoaderServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'FetchData': grpc.unary_unary_rpc_method_handler(
          servicer.FetchData,
          request_deserializer=dataLoader__pb2.TaskDataRequest.FromString,
          response_serializer=dataLoader__pb2.TaskDataReply.SerializeToString,
      ),
      'FetchDataAsStream': grpc.unary_stream_rpc_method_handler(
          servicer.FetchDataAsStream,
          request_deserializer=dataLoader__pb2.TaskDataRequest.FromString,
          response_serializer=dataLoader__pb2.TaskDataReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'BSU.DataLoader.DataLoader', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))