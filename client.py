import grpc

# import the generated classes
from proto import calculator_pb2
from proto import calculator_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = calculator_pb2_grpc.CalculatorStub(channel)

response = stub.SquareRoot(calculator_pb2.Number(value=16))
print(response.value)

response = stub.SquareRoot(calculator_pb2.Number(value=27))
print(response.value)

response = stub.SquareRoot(calculator_pb2.Number(value='27'))
print(response.value)
