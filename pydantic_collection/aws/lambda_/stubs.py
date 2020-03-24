from typing import Dict


class ClientContext:
    """ (mobile apps) Client context that's provided to Lambda by the client application."""

    @property
    def cognito_identity_pool_id(self) -> str:
        """The Amazon Cognito identity pool that authorized the invocation."""
        raise NotImplemented

    @property
    def installation_id(self) -> str:
        raise NotImplemented

    @property
    def app_title(self) -> str:
        raise NotImplemented

    @property
    def app_version_name(self) -> str:
        raise NotImplemented

    @property
    def app_version_code(self) -> str:
        raise NotImplemented

    @property
    def app_package_name(self) -> str:
        raise NotImplemented

    @property
    def custom(self) -> Dict:
        """A dict of custom values set by the mobile client application."""
        raise NotImplemented

    @property
    def env(self) -> Dict:
        """A dict of environment information provided by the AWS SDK."""
        raise NotImplemented


class Identity:
    """(mobile apps) Information about the Amazon Cognito identity that authorized the request."""

    @property
    def cognito_identity_id(self) -> str:
        """The authenticated Amazon Cognito identity."""
        raise NotImplemented

    @property
    def cognito_identity_pool_id(self) -> str:
        """The Amazon Cognito identity pool that authorized the invocation."""
        raise NotImplemented


class Context:
    def get_remaining_time_in_millis(self) -> int:
        """Returns the number of milliseconds left before the execution times out."""
        raise NotImplemented

    @property
    def function_name(self) -> str:
        """function_name – The name of the Lambda function."""
        raise NotImplemented

    @property
    def function_version(self) -> str:
        """The version of the function."""
        raise NotImplemented

    @property
    def invoked_function_arn(self) -> str:
        """The Amazon Resource Name (ARN) that's used to invoke the function."""
        raise NotImplemented

    @property
    def memory_limit_in_mb(self) -> int:
        """The amount of memory that's allocated for the function."""
        raise NotImplemented

    @property
    def aws_request_id(self) -> str:
        """The identifier of the invocation request."""
        raise NotImplemented

    @property
    def log_group_name(self) -> str:
        """The log group for the function."""
        raise NotImplemented

    @property
    def log_stream_name(self) -> str:
        """The log stream for the function instance."""
        raise NotImplemented

    @property
    def identity(self) -> Identity:
        """(mobile apps) Information about the Amazon Cognito identity that authorized the request."""
        raise NotImplemented

    @property
    def client_context(self) -> ClientContext:
        """ (mobile apps) Client context that's provided to Lambda by the client application."""
        raise NotImplemented
