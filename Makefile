.PHONY: proto
proto:
	python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. proto/*.proto
	@touch proto/__init__.py

.PHONY: gen_key
gen_key:
	openssl req -newkey rsa:2048 -nodes -keyout server.key -x509 -days 365 -out server.crt
