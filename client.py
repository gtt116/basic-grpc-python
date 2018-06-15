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


def get_insecure_stub():
    channel = grpc.insecure_channel('localhost:50051')
    stub = calculator_pb2_grpc.CalculatorStub(channel)
    return stub


def get_secure_stub():
    cre = get_server_credential()
    if cre is not None:
        channel = grpc.secure_channel('localhost:50050', cre)
        stub = calculator_pb2_grpc.CalculatorStub(channel)
        return stub
    return None


def get_server_credential():
    try:
        with open("server.crt", "rb") as f:
            return grpc.ssl_channel_credentials(root_certificates=f.read())
    except IOError:
        return None


def main():
    stub = get_insecure_stub()
    squareRoot(stub)
    sendEvent(stub)
    receiveEvents(stub)
    chat(stub)

    print("Now using secure channel")
    stub = get_secure_stub()
    squareRoot(stub)
    sendEvent(stub)
    receiveEvents(stub)
    chat(stub)


if __name__ == '__main__':
    main()
