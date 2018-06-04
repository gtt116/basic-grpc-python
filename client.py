import grpc
from google.protobuf import empty_pb2

# import the generated classes
from proto import calculator_pb2
from proto import calculator_pb2_grpc


def squareRoot(stub):
    response = stub.SquareRoot(calculator_pb2.Number(value=16))
    print(response.value)


def sendEvent(stub):
    def yieldEvents():
        for x in range(100, 111):
            yield calculator_pb2.Number(value=x)

    event_count = stub.SendEvents(yieldEvents())
    print("Total events: %s" % event_count)


def receiveEvents(stub):
    for x in stub.ReceiveEvents(empty_pb2.Empty()):
        print(x.value)


def chat(stub):
    def yieldMsg():
        for x in range(200, 300):
            yield calculator_pb2.Number(value=x)

    responses = stub.Chat(yieldMsg())
    for resp in responses:
        print("Receive response %s" % resp.value)


def main():
    channel = grpc.insecure_channel('localhost:50051')
    stub = calculator_pb2_grpc.CalculatorStub(channel)

    squareRoot(stub)
    sendEvent(stub)
    receiveEvents(stub)
    chat(stub)


if __name__ == '__main__':
    main()
