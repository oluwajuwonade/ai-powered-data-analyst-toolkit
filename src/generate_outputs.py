from __future__ import annotations

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA, OUTPUTS = ROOT / "data", ROOT / "outputs"
DATA.mkdir(exist_ok=True); OUTPUTS.mkdir(exist_ok=True)


def main() -> None:
    steps = pd.DataFrame({
        "stage": ["Frame", "Inspect", "Validate", "Analyse", "AI assist", "Verify", "Explain", "Preserve"],
        "owner": ["Analyst", "Analyst", "Analyst", "Analyst", "AI + analyst", "Analyst", "Analyst", "Analyst"],
        "automation_level": ["Low", "Medium", "Medium", "Medium", "High", "Low", "Low", "Medium"],
        "human_control_required": [1, 1, 1, 1, 1, 1, 1, 1],
        "reusable_asset": ["Question brief", "Data profile", "QA checklist", "KPI notebook", "Prompt module", "Evidence log", "Report memo", "Template"]
    })
    steps.to_csv(DATA / "workflow_stages.csv", index=False)
    effort = pd.DataFrame({"task": ["Data profiling", "KPI calculations", "Chart drafting", "Narrative first draft", "Quality assurance", "Evidence capture"], "before_hours": [2.5, 2.0, 1.5, 2.0, 1.0, 1.5], "after_hours": [1.0, 0.8, 0.6, 0.9, 1.0, 1.2]})
    effort["hours_saved"] = effort.before_hours - effort.after_hours
    effort["saving_pct"] = effort.hours_saved / effort.before_hours
    effort.to_csv(OUTPUTS / "workflow_effort_comparison.csv", index=False)
    checklist = pd.DataFrame({"control": ["Business question defined", "Data provenance recorded", "Schema validated", "KPI definitions documented", "AI-generated claims reviewed", "Material calculations re-performed", "Limitations stated", "Reusable asset saved"], "status": ["PASS"] * 8})
    checklist.to_csv(OUTPUTS / "qa_checklist.csv", index=False)
    total_before, total_after = effort.before_hours.sum(), effort.after_hours.sum()
    (OUTPUTS / "executive_summary.md").write_text(f"""# Executive Summary — Illustrative Analyst Workflow\n\n**Scope:** Demonstration of a repeatable analyst operating model using a synthetic effort comparison. This is not a measured productivity study.\n\n## Headline results\n\n- Illustrative workflow effort: **{total_before:.1f} hours → {total_after:.1f} hours**.\n- Implied setup-time reduction: **{(total_before-total_after)/total_before:.1%}**.\n- **8/8** quality-control checks are explicitly represented in the example checklist.\n\n## Decision readout\n\nAI assistance is positioned as bounded and reviewable: it can accelerate drafting, categorisation, and reusable setup, while business framing, material calculation verification, evidence review, and final recommendations remain human-controlled.\n\n## Limitations\n\nTime values are illustrative planning assumptions, not observed benchmarks. The toolkit does not claim that AI improves analytical accuracy without task-specific validation.\n""")

    plt.style.use("seaborn-v0_8-whitegrid")
    fig, ax = plt.subplots(figsize=(9, 5.2))
    x = range(len(effort)); width = .35
    ax.bar([i-width/2 for i in x], effort.before_hours, width, label="Before toolkit", color="#94A3B8")
    ax.bar([i+width/2 for i in x], effort.after_hours, width, label="With toolkit", color="#2563EB")
    ax.set_xticks(list(x)); ax.set_xticklabels(effort.task, rotation=25, ha="right"); ax.set_ylabel("Illustrative hours")
    ax.set_title("Illustrative Analyst Workflow Effort Comparison", loc="left", weight="bold"); ax.legend(frameon=False)
    fig.tight_layout(); fig.savefig(OUTPUTS / "workflow_effort_comparison.png", dpi=180); plt.close(fig)

    counts = steps.automation_level.value_counts().reindex(["Low", "Medium", "High"]).fillna(0)
    fig, ax = plt.subplots(figsize=(8, 4.8))
    ax.bar(counts.index, counts.values, color=["#C2413B", "#F59E0B", "#15803D"])
    ax.set_title("Automation Boundaries Across the Analyst Workflow", loc="left", weight="bold")
    ax.set_ylabel("Workflow stages"); ax.set_xlabel("Automation level")
    fig.tight_layout(); fig.savefig(OUTPUTS / "automation_boundaries.png", dpi=180); plt.close(fig)


if __name__ == "__main__":
    main()
