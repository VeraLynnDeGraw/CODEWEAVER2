"""CODEWEAVER2 Enhanced Data Models (Pydantic V2)"""
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, ConfigDict, Field, computed_field

class FindingState(str, Enum):
    THREAD = "thread"; NODE = "node"; JUNCTION = "junction"
    MAPPED = "mapped"; PATTERN = "pattern"; SIGNAL = "signal"
    BENIGN = "benign"; CONCERN = "concern"; WARNING = "warning"; CRITICAL = "critical"
    REINFORCE = "reinforce"; REPAIR = "repair"; AVOID = "avoid"; MONITOR = "monitor"
    STABLE = "stable"; FRAGILE = "fragile"; BROKEN = "broken"; UNKNOWN = "unknown"

    @property
    def icon(self) -> str:
        icons = {"thread": "🧵", "node": "🔵", "junction": "🔗", "mapped": "🗺️", "pattern": "🔍", 
                 "signal": "📡", "benign": "✅", "concern": "⚠️", "warning": "🚨", "critical": "🔴",
                 "reinforce": "💪", "repair": "🔧", "avoid": "🚫", "monitor": "👁️", "stable": "✨", 
                 "fragile": "⚡", "broken": "💥", "unknown": "❓"}
        return icons.get(self.value, "❓")

class Confidence(str, Enum):
    HIGH = "high"; MEDIUM = "medium"; LOW = "low"
    @property
    def icon(self) -> str: return {"high": "🟢", "medium": "🟡", "low": "🔴"}[self.value]

class ProposalPriority(str, Enum):
    CRITICAL = "critical"; HIGH = "high"; MEDIUM = "medium"; LOW = "low"
    @property
    def icon(self) -> str: return {"critical": "🔴", "high": "🟠", "medium": "🟡", "low": "🟢"}[self.value]
    @property
    def numeric_value(self) -> int: return {"critical": 4, "high": 3, "medium": 2, "low": 1}[self.value]

class WeaverBaseModel(BaseModel):
    model_config = ConfigDict(frozen=True, validate_assignment=True, str_strip_whitespace=True)

class Finding(WeaverBaseModel):
    finding_id: str
    state: FindingState
    subject: str
    value: str
    source: str
    confidence: Confidence
    reason: str
    tags: List[str] = Field(default_factory=list)

class Proposal(WeaverBaseModel):
    proposal_id: str
    title: str
    tldr: str
    description: str
    impact_score: int = Field(5, ge=1, le=10)
    effort_score: int = Field(3, ge=1, le=10)
    priority: ProposalPriority = ProposalPriority.MEDIUM
    supporting_findings: List[Finding] = Field(default_factory=list)

    @computed_field
    @property
    def is_quick_win(self) -> bool:
        return self.impact_score >= 7 and self.effort_score <= 3

class DashboardMetrics(WeaverBaseModel):
    total_files_analyzed: int = 0
    total_findings: int = 0
    total_proposals: int = 0
    quick_wins: int = 0
    critical_proposals: int = 0
    overall_health_score: float = Field(78.0, ge=0.0, le=100.0)

class ProjectContext(WeaverBaseModel):
    root_path: str
    analysis_timestamp: datetime = Field(default_factory=datetime.now)
    findings: List[Finding] = Field(default_factory=list)
    proposals: List[Proposal] = Field(default_factory=list)
    metrics: DashboardMetrics = Field(default_factory=DashboardMetrics)
