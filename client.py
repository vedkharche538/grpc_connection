import grpc
import grpc_pb2
import grpc_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = grpc_pb2_grpc.ExampleServiceStub(channel)
        response = stub.SayHello(grpc_pb2.HelloRequest(name="Alice"))
        print("Server response:", response.message)

if __name__ == '__main__':
    run()
