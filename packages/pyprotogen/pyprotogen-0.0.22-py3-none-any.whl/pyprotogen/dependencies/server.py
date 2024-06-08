from grpc.aio import server, Server
from grpc_prometheus_metrics.aio.prometheus_aio_server_interceptor import PromAioServerInterceptor


def get_server(enable_metrics: bool = True) -> Server:
    interceptors = []
    if enable_metrics:
        prom = PromAioServerInterceptor(enable_handling_time_histogram=True)
        interceptors.append(prom)
    return server(interceptors=interceptors)
