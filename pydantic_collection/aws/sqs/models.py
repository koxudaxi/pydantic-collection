from typing import Any, Dict, List

from pydantic import BaseModel


class Attributes(BaseModel):
    ApproximateReceiveCount: int
    SentTimestamp: int
    SequenceNumber: int
    MessageGroupId: str
    SenderId: str
    MessageDeduplicationId: str
    ApproximateFirstReceiveTimestamp: str


class Record(BaseModel):
    messageId: str
    receiptHandle: str
    body: str
    attributes: Attributes
    messageAttributes: Dict[str, Any]
    md5OfBody: str
    eventSource: str
    eventSourceARN: str
    awsRegion: str


class Event(BaseModel):
    Records: List[Record]
