"""Basic tests for CODEWEAVER2 models"""
from codeweaver2.models import (
    FindingState, Confidence, ProposalPriority,
    Finding, Proposal, DashboardMetrics, ProjectContext
)

def test_finding_state_icons():
    """Test that all finding states have icons"""
    assert FindingState.THREAD.icon == "🧵"
    assert FindingState.CRITICAL.icon == "🔴"
    assert FindingState.STABLE.icon == "✨"

def test_confidence_icons():
    """Test confidence level icons"""
    assert Confidence.HIGH.icon == "🟢"
    assert Confidence.MEDIUM.icon == "🟡"
    assert Confidence.LOW.icon == "🔴"

def test_proposal_quick_win():
    """Test quick win detection logic"""
    proposal = Proposal(
        proposal_id="test-001",
        title="Test Quick Win",
        tldr="Test description",
        description="Full description",
        impact_score=9,
        effort_score=2,
        priority=ProposalPriority.HIGH
    )
    assert proposal.is_quick_win is True

def test_dashboard_metrics_defaults():
    """Test dashboard metrics default values"""
    metrics = DashboardMetrics()
    assert metrics.total_files_analyzed == 0
    assert metrics.overall_health_score == 78.0

def test_project_context_creation():
    """Test creating a project context"""
    ctx = ProjectContext(root_path="/test/path")
    assert ctx.root_path == "/test/path"
    assert ctx.analysis_timestamp is not None
    assert len(ctx.findings) == 0
    assert len(ctx.proposals) == 0
