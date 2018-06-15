.PHONY: proto
proto:
	python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. proto/*.proto
	@touch proto/__init__.py

.PHONY: gen_key
gen_key:
	# NOTE: Please remember to set common name to "localhost", otherwise connection will failed by
	# (StatusCode.UNAVAILABLE, Connect Failed)
	openssl req -newkey rsa:2048 -nodes -keyout server.key -x509 -days 365 -out server.crt
