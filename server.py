import grpc
from concurrent import futures
import grpc_pb2
import grpc_pb2_grpc

class ExampleServiceServicer(grpc_pb2_grpc.ExampleServiceServicer):
    def SayHello(self, request, context):
        reply = f"Hello, {request.name}!"
        return grpc_pb2.HelloReply(message=reply)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    grpc_pb2_grpc.add_ExampleServiceServicer_to_server(ExampleServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
