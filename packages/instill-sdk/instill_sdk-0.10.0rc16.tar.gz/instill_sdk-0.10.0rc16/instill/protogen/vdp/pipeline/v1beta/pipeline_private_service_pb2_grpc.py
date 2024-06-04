# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from vdp.pipeline.v1beta import pipeline_pb2 as vdp_dot_pipeline_dot_v1beta_dot_pipeline__pb2


class PipelinePrivateServiceStub(object):
    """PipelinePrivateService defines private methods to interact with Pipeline
    resources.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListPipelinesAdmin = channel.unary_unary(
                '/vdp.pipeline.v1beta.PipelinePrivateService/ListPipelinesAdmin',
                request_serializer=vdp_dot_pipeline_dot_v1beta_dot_pipeline__pb2.ListPipelinesAdminRequest.SerializeToString,
                response_deserializer=vdp_dot_pipeline_dot_v1beta_dot_pipeline__pb2.ListPipelinesAdminResponse.FromString,
                )
        self.LookUpPipelineAdmin = channel.unary_unary(
                '/vdp.pipeline.v1beta.PipelinePrivateService/LookUpPipelineAdmin',
                request_serializer=vdp_dot_pipeline_dot_v1beta_dot_pipeline__pb2.LookUpPipelineAdminRequest.SerializeToString,
                response_deserializer=vdp_dot_pipeline_dot_v1beta_dot_pipeline__pb2.LookUpPipelineAdminResponse.FromString,
                )
        self.ListPipelineReleasesAdmin = channel.unary_unary(
                '/vdp.pipeline.v1beta.PipelinePrivateService/ListPipelineReleasesAdmin',
                request_serializer=vdp_dot_pipeline_dot_v1beta_dot_pipeline__pb2.ListPipelineReleasesAdminRequest.SerializeToString,
                response_deserializer=vdp_dot_pipeline_dot_v1beta_dot_pipeline__pb2.ListPipelineReleasesAdminResponse.FromString,
                )


class PipelinePrivateServiceServicer(object):
    """PipelinePrivateService defines private methods to interact with Pipeline
    resources.
    """

    def ListPipelinesAdmin(self, request, context):
        """List pipelines (admin only)

        This is a *private* method that allows admin users and internal clients to
        list *all* pipeline resources.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LookUpPipelineAdmin(self, request, context):
        """Get a pipeline by UID (admin only)

        This is a *private* method that allows admin users to access any pipeline
        resource by its UID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListPipelineReleasesAdmin(self, request, context):
        """List pipeline releases (admin only)

        This is a *private* method that allows admin users to list *all* pipeline
        releases.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PipelinePrivateServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListPipelinesAdmin': grpc.unary_unary_rpc_method_handler(
                    servicer.ListPipelinesAdmin,
                    request_deserializer=vdp_dot_pipeline_dot_v1beta_dot_pipeline__pb2.ListPipelinesAdminRequest.FromString,
                    response_serializer=vdp_dot_pipeline_dot_v1beta_dot_pipeline__pb2.ListPipelinesAdminResponse.SerializeToString,
            ),
            'LookUpPipelineAdmin': grpc.unary_unary_rpc_method_handler(
                    servicer.LookUpPipelineAdmin,
                    request_deserializer=vdp_dot_pipeline_dot_v1beta_dot_pipeline__pb2.LookUpPipelineAdminRequest.FromString,
                    response_serializer=vdp_dot_pipeline_dot_v1beta_dot_pipeline__pb2.LookUpPipelineAdminResponse.SerializeToString,
            ),
            'ListPipelineReleasesAdmin': grpc.unary_unary_rpc_method_handler(
                    servicer.ListPipelineReleasesAdmin,
                    request_deserializer=vdp_dot_pipeline_dot_v1beta_dot_pipeline__pb2.ListPipelineReleasesAdminRequest.FromString,
                    response_serializer=vdp_dot_pipeline_dot_v1beta_dot_pipeline__pb2.ListPipelineReleasesAdminResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'vdp.pipeline.v1beta.PipelinePrivateService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PipelinePrivateService(object):
    """PipelinePrivateService defines private methods to interact with Pipeline
    resources.
    """

    @staticmethod
    def ListPipelinesAdmin(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vdp.pipeline.v1beta.PipelinePrivateService/ListPipelinesAdmin',
            vdp_dot_pipeline_dot_v1beta_dot_pipeline__pb2.ListPipelinesAdminRequest.SerializeToString,
            vdp_dot_pipeline_dot_v1beta_dot_pipeline__pb2.ListPipelinesAdminResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LookUpPipelineAdmin(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vdp.pipeline.v1beta.PipelinePrivateService/LookUpPipelineAdmin',
            vdp_dot_pipeline_dot_v1beta_dot_pipeline__pb2.LookUpPipelineAdminRequest.SerializeToString,
            vdp_dot_pipeline_dot_v1beta_dot_pipeline__pb2.LookUpPipelineAdminResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListPipelineReleasesAdmin(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/vdp.pipeline.v1beta.PipelinePrivateService/ListPipelineReleasesAdmin',
            vdp_dot_pipeline_dot_v1beta_dot_pipeline__pb2.ListPipelineReleasesAdminRequest.SerializeToString,
            vdp_dot_pipeline_dot_v1beta_dot_pipeline__pb2.ListPipelineReleasesAdminResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
