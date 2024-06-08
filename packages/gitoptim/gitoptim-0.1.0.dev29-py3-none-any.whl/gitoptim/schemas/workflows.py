from pydantic import BaseModel


class AnalyseLogsSchema(BaseModel):
    logs: str
    pipeline_id: int
    job_id: int
    commit_ref: str
    branch_ref: str
    event_type: str = "gitlab-job-logs"
