# Generated by ariadne-codegen
# Source: operations.graphql

from typing import Optional

from stigg._vendors.pydantic import Field

from .base_model import BaseModel


class ReportEvent(BaseModel):
    report_event: Optional[str] = Field(alias="reportEvent")
