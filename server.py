import grpc
from concurrent import futures
import time

from proto import calculator_pb2
from proto import calculator_pb2_grpc


class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):

    def SquareRoot(self, request, context):
        response = calculator_pb2.Number()
        response.value = (request.value) * (request.value)
        return response

    def ReceiveEvents(self, request, context):
        for x in range(10):
            yield calculator_pb2.Number(value=x)
            time.sleep(0.3)

    def SendEvents(self, request_iterator, context):
        count = 0
        for req in request_iterator:
            print("Receive: %s, context: %s" % (req.value, context))
            count += 1
        return calculator_pb2.Number(value=count)

    def Chat(self, request_iterator, context):
        for req in request_iterator:
            yield calculator_pb2.Number(value=(req.value + 11))


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)

    print('Starting server. Listening on port 50051.')
    server.add_insecure_port('[::]:50051')
    server.start()

    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    main()
