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
