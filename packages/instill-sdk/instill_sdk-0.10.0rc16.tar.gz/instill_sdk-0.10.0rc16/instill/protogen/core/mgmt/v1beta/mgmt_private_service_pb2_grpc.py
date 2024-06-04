# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from core.mgmt.v1beta import mgmt_pb2 as core_dot_mgmt_dot_v1beta_dot_mgmt__pb2


class MgmtPrivateServiceStub(object):
    """Mgmt service responds to internal access
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListUsersAdmin = channel.unary_unary(
                '/core.mgmt.v1beta.MgmtPrivateService/ListUsersAdmin',
                request_serializer=core_dot_mgmt_dot_v1beta_dot_mgmt__pb2.ListUsersAdminRequest.SerializeToString,
                response_deserializer=core_dot_mgmt_dot_v1beta_dot_mgmt__pb2.ListUsersAdminResponse.FromString,
                )
        self.GetUserAdmin = channel.unary_unary(
                '/core.mgmt.v1beta.MgmtPrivateService/GetUserAdmin',
                request_serializer=core_dot_mgmt_dot_v1beta_dot_mgmt__pb2.GetUserAdminRequest.SerializeToString,
                response_deserializer=core_dot_mgmt_dot_v1beta_dot_mgmt__pb2.GetUserAdminResponse.FromString,
                )
        self.LookUpUserAdmin = channel.unary_unary(
                '/core.mgmt.v1beta.MgmtPrivateService/LookUpUserAdmin',
                request_serializer=core_dot_mgmt_dot_v1beta_dot_mgmt__pb2.LookUpUserAdminRequest.SerializeToString,
                response_deserializer=core_dot_mgmt_dot_v1beta_dot_mgmt__pb2.LookUpUserAdminResponse.FromString,
                )
        self.ListOrganizationsAdmin = channel.unary_unary(
                '/core.mgmt.v1beta.MgmtPrivateService/ListOrganizationsAdmin',
                request_serializer=core_dot_mgmt_dot_v1beta_dot_mgmt__pb2.ListOrganizationsAdminRequest.SerializeToString,
                response_deserializer=core_dot_mgmt_dot_v1beta_dot_mgmt__pb2.ListOrganizationsAdminResponse.FromString,
                )
        self.GetOrganizationAdmin = channel.unary_unary(
                '/core.mgmt.v1beta.MgmtPrivateService/GetOrganizationAdmin',
                request_serializer=core_dot_mgmt_dot_v1beta_dot_mgmt__pb2.GetOrganizationAdminRequest.SerializeToString,
                response_deserializer=core_dot_mgmt_dot_v1beta_dot_mgmt__pb2.GetOrganizationAdminResponse.FromString,
                )
        self.LookUpOrganizationAdmin = channel.unary_unary(
                '/core.mgmt.v1beta.MgmtPrivateService/LookUpOrganizationAdmin',
                request_serializer=core_dot_mgmt_dot_v1beta_dot_mgmt__pb2.LookUpOrganizationAdminRequest.SerializeToString,
                response_deserializer=core_dot_mgmt_dot_v1beta_dot_mgmt__pb2.LookUpOrganizationAdminResponse.FromString,
                )
        self.GetUserSubscriptionAdmin = channel.unary_unary(
                '/core.mgmt.v1beta.MgmtPrivateService/GetUserSubscriptionAdmin',
                request_serializer=core_dot_mgmt_dot_v1beta_dot_mgmt__pb2.GetUserSubscriptionAdminRequest.SerializeToString,
                response_deserializer=core_dot_mgmt_dot_v1beta_dot_mgmt__pb2.GetUserSubscriptionAdminResponse.FromString,
                )
        self.GetOrganizationSubscriptionAdmin = channel.unary_unary(
                '/core.mgmt.v1beta.MgmtPrivateService/GetOrganizationSubscriptionAdmin',
                request_serializer=core_dot_mgmt_dot_v1beta_dot_mgmt__pb2.GetOrganizationSubscriptionAdminRequest.SerializeToString,
                response_deserializer=core_dot_mgmt_dot_v1beta_dot_mgmt__pb2.GetOrganizationSubscriptionAdminResponse.FromString,
                )
        self.SubtractCredit = channel.unary_unary(
                '/core.mgmt.v1beta.MgmtPrivateService/SubtractCredit',
                request_serializer=core_dot_mgmt_dot_v1beta_dot_mgmt__pb2.SubtractCreditRequest.SerializeToString,
                response_deserializer=core_dot_mgmt_dot_v1beta_dot_mgmt__pb2.SubtractCreditResponse.FromString,
                )


class MgmtPrivateServiceServicer(object):
    """Mgmt service responds to internal access
    """

    def ListUsersAdmin(self, request, context):
        """ListUsersAdmin method receives a ListUsersAdminRequest message and returns
        a ListUsersAdminResponse message.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUserAdmin(self, request, context):
        """GetUserAdmin method receives a GetUserAdminRequest message and returns
        a GetUserAdminResponse message.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LookUpUserAdmin(self, request, context):
        """LookUpUserAdmin method receives a LookUpUserAdminRequest message and
        returns a LookUpUserAdminResponse
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListOrganizationsAdmin(self, request, context):
        """ListOrganizationsAdmin method receives a ListOrganizationsAdminRequest message and returns
        a ListOrganizationsAdminResponse message.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOrganizationAdmin(self, request, context):
        """GetOrganizationAdmin method receives a GetOrganizationAdminRequest message and returns
        a GetOrganizationAdminResponse message.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LookUpOrganizationAdmin(self, request, context):
        """LookUpOrganizationAdmin method receives a LookUpOrganizationAdminRequest message and
        returns a LookUpOrganizationAdminResponse
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUserSubscriptionAdmin(self, request, context):
        """GetUserSubscriptionAdmin
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOrganizationSubscriptionAdmin(self, request, context):
        """GetOrganizationSubscriptionAdmin
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubtractCredit(self, request, context):
        """Subtract Instill Credit from a user or organization account.

        This endpoint subtracts the specified amount of Instill Credit from an
        account. This is intended for processes on Instill Cloud that consume
        credit, such as the execution of pre-configured connectors.
        Note that if the remaining credit in the account is less than the
        requested amount, it will be subtracted anyways, leaving the account
        credit at zero. A ResourceExhausted error will be returned in this case.

        On Instill Core, this endpoint will return an Unimplemented status.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MgmtPrivateServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ListUsersAdmin': grpc.unary_unary_rpc_method_handler(
                    servicer.ListUsersAdmin,
                    request_deserializer=core_dot_mgmt_dot_v1beta_dot_mgmt__pb2.ListUsersAdminRequest.FromString,
                    response_serializer=core_dot_mgmt_dot_v1beta_dot_mgmt__pb2.ListUsersAdminResponse.SerializeToString,
            ),
            'GetUserAdmin': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUserAdmin,
                    request_deserializer=core_dot_mgmt_dot_v1beta_dot_mgmt__pb2.GetUserAdminRequest.FromString,
                    response_serializer=core_dot_mgmt_dot_v1beta_dot_mgmt__pb2.GetUserAdminResponse.SerializeToString,
            ),
            'LookUpUserAdmin': grpc.unary_unary_rpc_method_handler(
                    servicer.LookUpUserAdmin,
                    request_deserializer=core_dot_mgmt_dot_v1beta_dot_mgmt__pb2.LookUpUserAdminRequest.FromString,
                    response_serializer=core_dot_mgmt_dot_v1beta_dot_mgmt__pb2.LookUpUserAdminResponse.SerializeToString,
            ),
            'ListOrganizationsAdmin': grpc.unary_unary_rpc_method_handler(
                    servicer.ListOrganizationsAdmin,
                    request_deserializer=core_dot_mgmt_dot_v1beta_dot_mgmt__pb2.ListOrganizationsAdminRequest.FromString,
                    response_serializer=core_dot_mgmt_dot_v1beta_dot_mgmt__pb2.ListOrganizationsAdminResponse.SerializeToString,
            ),
            'GetOrganizationAdmin': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOrganizationAdmin,
                    request_deserializer=core_dot_mgmt_dot_v1beta_dot_mgmt__pb2.GetOrganizationAdminRequest.FromString,
                    response_serializer=core_dot_mgmt_dot_v1beta_dot_mgmt__pb2.GetOrganizationAdminResponse.SerializeToString,
            ),
            'LookUpOrganizationAdmin': grpc.unary_unary_rpc_method_handler(
                    servicer.LookUpOrganizationAdmin,
                    request_deserializer=core_dot_mgmt_dot_v1beta_dot_mgmt__pb2.LookUpOrganizationAdminRequest.FromString,
                    response_serializer=core_dot_mgmt_dot_v1beta_dot_mgmt__pb2.LookUpOrganizationAdminResponse.SerializeToString,
            ),
            'GetUserSubscriptionAdmin': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUserSubscriptionAdmin,
                    request_deserializer=core_dot_mgmt_dot_v1beta_dot_mgmt__pb2.GetUserSubscriptionAdminRequest.FromString,
                    response_serializer=core_dot_mgmt_dot_v1beta_dot_mgmt__pb2.GetUserSubscriptionAdminResponse.SerializeToString,
            ),
            'GetOrganizationSubscriptionAdmin': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOrganizationSubscriptionAdmin,
                    request_deserializer=core_dot_mgmt_dot_v1beta_dot_mgmt__pb2.GetOrganizationSubscriptionAdminRequest.FromString,
                    response_serializer=core_dot_mgmt_dot_v1beta_dot_mgmt__pb2.GetOrganizationSubscriptionAdminResponse.SerializeToString,
            ),
            'SubtractCredit': grpc.unary_unary_rpc_method_handler(
                    servicer.SubtractCredit,
                    request_deserializer=core_dot_mgmt_dot_v1beta_dot_mgmt__pb2.SubtractCreditRequest.FromString,
                    response_serializer=core_dot_mgmt_dot_v1beta_dot_mgmt__pb2.SubtractCreditResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'core.mgmt.v1beta.MgmtPrivateService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MgmtPrivateService(object):
    """Mgmt service responds to internal access
    """

    @staticmethod
    def ListUsersAdmin(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/core.mgmt.v1beta.MgmtPrivateService/ListUsersAdmin',
            core_dot_mgmt_dot_v1beta_dot_mgmt__pb2.ListUsersAdminRequest.SerializeToString,
            core_dot_mgmt_dot_v1beta_dot_mgmt__pb2.ListUsersAdminResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUserAdmin(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/core.mgmt.v1beta.MgmtPrivateService/GetUserAdmin',
            core_dot_mgmt_dot_v1beta_dot_mgmt__pb2.GetUserAdminRequest.SerializeToString,
            core_dot_mgmt_dot_v1beta_dot_mgmt__pb2.GetUserAdminResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LookUpUserAdmin(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/core.mgmt.v1beta.MgmtPrivateService/LookUpUserAdmin',
            core_dot_mgmt_dot_v1beta_dot_mgmt__pb2.LookUpUserAdminRequest.SerializeToString,
            core_dot_mgmt_dot_v1beta_dot_mgmt__pb2.LookUpUserAdminResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListOrganizationsAdmin(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/core.mgmt.v1beta.MgmtPrivateService/ListOrganizationsAdmin',
            core_dot_mgmt_dot_v1beta_dot_mgmt__pb2.ListOrganizationsAdminRequest.SerializeToString,
            core_dot_mgmt_dot_v1beta_dot_mgmt__pb2.ListOrganizationsAdminResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetOrganizationAdmin(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/core.mgmt.v1beta.MgmtPrivateService/GetOrganizationAdmin',
            core_dot_mgmt_dot_v1beta_dot_mgmt__pb2.GetOrganizationAdminRequest.SerializeToString,
            core_dot_mgmt_dot_v1beta_dot_mgmt__pb2.GetOrganizationAdminResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LookUpOrganizationAdmin(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/core.mgmt.v1beta.MgmtPrivateService/LookUpOrganizationAdmin',
            core_dot_mgmt_dot_v1beta_dot_mgmt__pb2.LookUpOrganizationAdminRequest.SerializeToString,
            core_dot_mgmt_dot_v1beta_dot_mgmt__pb2.LookUpOrganizationAdminResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUserSubscriptionAdmin(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/core.mgmt.v1beta.MgmtPrivateService/GetUserSubscriptionAdmin',
            core_dot_mgmt_dot_v1beta_dot_mgmt__pb2.GetUserSubscriptionAdminRequest.SerializeToString,
            core_dot_mgmt_dot_v1beta_dot_mgmt__pb2.GetUserSubscriptionAdminResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetOrganizationSubscriptionAdmin(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/core.mgmt.v1beta.MgmtPrivateService/GetOrganizationSubscriptionAdmin',
            core_dot_mgmt_dot_v1beta_dot_mgmt__pb2.GetOrganizationSubscriptionAdminRequest.SerializeToString,
            core_dot_mgmt_dot_v1beta_dot_mgmt__pb2.GetOrganizationSubscriptionAdminResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubtractCredit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/core.mgmt.v1beta.MgmtPrivateService/SubtractCredit',
            core_dot_mgmt_dot_v1beta_dot_mgmt__pb2.SubtractCreditRequest.SerializeToString,
            core_dot_mgmt_dot_v1beta_dot_mgmt__pb2.SubtractCreditResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
