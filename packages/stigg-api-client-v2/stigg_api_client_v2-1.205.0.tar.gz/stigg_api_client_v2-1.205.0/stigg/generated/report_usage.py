# Generated by ariadne-codegen
# Source: operations.graphql

from stigg._vendors.pydantic import Field

from .base_model import BaseModel
from .fragments import ReportUsageFragment


class ReportUsage(BaseModel):
    report_usage: "ReportUsageReportUsage" = Field(alias="reportUsage")


class ReportUsageReportUsage(ReportUsageFragment):
    pass


ReportUsage.model_rebuild()
