import boto3
import datetime
from enum import Enum
from pydantic import BaseModel


class StreamlineLogLevel(str, Enum):
    INFO = "INFO"
    ERROR = "ERROR"
    WARN = "WARN"


class GetOrCreateLogStreamParams(BaseModel):
    log_group_name: str
    log_stream_name: str


class LogParams(BaseModel):
    log_group_name: str
    log_stream_name: str
    log_level: StreamlineLogLevel
    message: str


class StreamlineLogger:
    def __init__(self, environment: str, cloudwatch_logs: boto3.client = None):
        if environment == "production" and cloudwatch_logs is None:
            raise ValueError(
                "CloudWatchLogs is required in production environment"
            )

        self.environment = environment
        self.cloudwatch_logs = cloudwatch_logs

    def get_or_create_log_stream(
        self, params: GetOrCreateLogStreamParams
    ) -> str:
        if self.environment == "development":
            return params.log_stream_name

        if self.cloudwatch_logs is None:
            raise ValueError(
                "CloudWatchLogs is required in production environment"
            )

        describe_res = self.cloudwatch_logs.describe_log_streams(
            logGroupName=params.log_group_name,
            logStreamNamePrefix=params.log_stream_name,
        )

        log_stream_exists = len(describe_res["logStreams"]) != 0

        if not log_stream_exists:
            self.cloudwatch_logs.create_log_stream(
                logGroupName=params.log_group_name,
                logStreamName=params.log_stream_name,
            )

        return params.log_stream_name

    def log(self, params: LogParams):
        if self.environment == "development":
            print(
                f"[{datetime.datetime.now().timestamp()}] "
                + f"{params.log_level}: {params.message}"
            )
            return

        if self.cloudwatch_logs is None:
            raise ValueError(
                "CloudWatchLogs is required in production environment"
            )

        send_cloudwatch_log(
            self.cloudwatch_logs,
            params.log_group_name,
            params.log_stream_name,
            params.log_level,
            params.message,
        )


def send_cloudwatch_log(
    cloudwatch_logs, log_group_name, log_stream_name, log_level, message
):
    cloudwatch_logs.put_log_events(
        logGroupName=log_group_name,
        logStreamName=log_stream_name,
        logEvents=[
            {
                "message": f"{log_level.value}: {message}",
                "timestamp": int(datetime.datetime.now().timestamp() * 1000),
            }
        ],
    )
