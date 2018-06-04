.PHONY: proto
proto:
	python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. proto/*.proto
	@touch proto/__init__.py
