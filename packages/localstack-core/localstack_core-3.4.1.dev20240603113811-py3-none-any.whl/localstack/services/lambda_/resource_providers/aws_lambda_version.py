# LocalStack Resource Provider Scaffolding v2
from __future__ import annotations

from pathlib import Path
from typing import Optional, TypedDict

import localstack.services.cloudformation.provider_utils as util
from localstack.services.cloudformation.resource_provider import (
    OperationStatus,
    ProgressEvent,
    ResourceProvider,
    ResourceRequest,
)


class LambdaVersionProperties(TypedDict):
    FunctionName: Optional[str]
    CodeSha256: Optional[str]
    Description: Optional[str]
    Id: Optional[str]
    ProvisionedConcurrencyConfig: Optional[ProvisionedConcurrencyConfiguration]
    Version: Optional[str]


class ProvisionedConcurrencyConfiguration(TypedDict):
    ProvisionedConcurrentExecutions: Optional[int]


REPEATED_INVOCATION = "repeated_invocation"


class LambdaVersionProvider(ResourceProvider[LambdaVersionProperties]):
    TYPE = "AWS::Lambda::Version"  # Autogenerated. Don't change
    SCHEMA = util.get_schema_path(Path(__file__))  # Autogenerated. Don't change

    def create(
        self,
        request: ResourceRequest[LambdaVersionProperties],
    ) -> ProgressEvent[LambdaVersionProperties]:
        """
        Create a new resource.

        Primary identifier fields:
          - /properties/Id

        Required properties:
          - FunctionName

        Create-only properties:
          - /properties/FunctionName

        Read-only properties:
          - /properties/Id
          - /properties/Version



        """
        model = request.desired_state
        lambda_client = request.aws_client_factory.lambda_
        ctx = request.custom_context

        params = util.select_attributes(model, ["FunctionName", "CodeSha256", "Description"])

        if not ctx.get(REPEATED_INVOCATION):
            response = lambda_client.publish_version(**params)
            model["Version"] = response["Version"]
            model["Id"] = response["FunctionArn"]
            ctx[REPEATED_INVOCATION] = True
            return ProgressEvent(
                status=OperationStatus.IN_PROGRESS,
                resource_model=model,
                custom_context=request.custom_context,
            )

        version = lambda_client.get_function(FunctionName=model["Id"])
        if version["Configuration"]["State"] == "Pending":
            return ProgressEvent(
                status=OperationStatus.IN_PROGRESS,
                resource_model=model,
                custom_context=request.custom_context,
            )
        elif version["Configuration"]["State"] == "Active":
            return ProgressEvent(
                status=OperationStatus.SUCCESS,
                resource_model=model,
            )
        else:
            return ProgressEvent(
                status=OperationStatus.FAILED,
                resource_model=model,
                message="",
                error_code="VersionStateFailure",  # TODO: not parity tested
            )

    def read(
        self,
        request: ResourceRequest[LambdaVersionProperties],
    ) -> ProgressEvent[LambdaVersionProperties]:
        """
        Fetch resource information


        """
        raise NotImplementedError

    def delete(
        self,
        request: ResourceRequest[LambdaVersionProperties],
    ) -> ProgressEvent[LambdaVersionProperties]:
        """
        Delete a resource


        """
        model = request.desired_state
        lambda_client = request.aws_client_factory.lambda_

        # without qualifier entire function is deleted instead of just version
        lambda_client.delete_function(FunctionName=model["Id"], Qualifier=model["Version"])

        return ProgressEvent(
            status=OperationStatus.SUCCESS,
            resource_model=model,
            custom_context=request.custom_context,
        )

    def update(
        self,
        request: ResourceRequest[LambdaVersionProperties],
    ) -> ProgressEvent[LambdaVersionProperties]:
        """
        Update a resource


        """
        raise NotImplementedError
