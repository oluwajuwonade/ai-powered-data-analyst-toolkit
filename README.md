# AI-Native Data Analyst Operating System

> **Workflow problem:** Which analyst activities can be accelerated with AI without weakening analytical quality or human accountability?

A reusable operating system for analysts combining data workflows, AI prompt modules, reporting templates, and explicit quality-control boundaries.

## Operating workflow

`Ingest → Profile → Clean → Explore → Analyse → Validate → Explain → Report`

AI is treated as an accelerator inside the workflow, not as a substitute for validation or judgment.

## Analytical questions

1. Which analyst tasks can be standardized safely?
2. Where can AI reduce repetitive effort?
3. Which checks must remain human-controlled?
4. Which analytical outputs can become reusable assets?

## Components

- Data-cleaning workflow
- KPI-analysis workflow
- EDA checklist
- AI prompt modules
- Report skeleton
- QA checklist
- Reusable templates
- Workflow control matrix

## Human-control boundary

The toolkit explicitly distinguishes:

**AI-assisted:** drafting, classification, pattern discovery, documentation, transformation suggestions.

**Human-controlled:** evidence validation, causal claims, business interpretation, final recommendations, consequential decisions.

## Reproduce

Run:

```bash
python src/generate_outputs.py
```

The generated outputs illustrate workflow stages, control ownership, and an example effort comparison.

## Data disclosure

The effort comparisons are planning assumptions used to explain workflow design. They are **not observed productivity benchmarks**.

## Important limitations

- Effort comparisons are planning assumptions, not observed productivity benchmarks.
- AI-assisted steps can introduce omission, hallucination, or interpretation errors and require human validation.
- The toolkit is a reusable workflow framework, not a guarantee of faster or better analysis in every context.
- Consequential analytical decisions remain subject to source-data quality, domain context, and human review.

## Portfolio role

**Tier 2 — AI-Powered Analytics Infrastructure**

This project demonstrates workflow design and responsible use of AI inside analytical work.

## Related projects

- [AI Research & Evaluation Framework](https://github.com/oluwajuwonade/ai-research-evaluation-system)
- [Data Quality & Analytics Assurance](https://github.com/oluwajuwonade/data-quality-audit-toolkit)
- [AI-Powered Retail Sales Diagnostic](https://github.com/oluwajuwonade/AI-Powered-Retail-Sales-Diagnostic)

## Author

**Oluwajuwon Adediji**  
Data & Quantitative Analyst | AI-Powered Analytics | Workflow Automation
