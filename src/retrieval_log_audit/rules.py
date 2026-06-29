from __future__ import annotations

from retrieval_log_audit.models import Rule

PROJECT_NAME = 'retrieval-log-audit'
DESCRIPTION = 'Find retrieval logs with empty hits, weak scores, and missing source metadata.'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "service", "dataset", "route", "metric", "field", "path")
HIGH_SAMPLE = 'query password reset hits: 0 top_score: 0.12 source: missing'
MEDIUM_SAMPLE = '\\b(top_score|score)\\s*[:=]\\s*0\\.[01][0-9]\\b'
CLEAN_SAMPLE = 'query password reset hits 5 top_score 0.82 source docs/password.md'

RULES = (
    Rule(
        code='empty-retrieval',
        severity='high',
        pattern='\\b(hits\\s*[:=]\\s*0|no documents|empty retrieval)\\b',
        message='retrieval returned no documents',
        recommendation='Add coverage or route query to fallback handling.',
    ),
    Rule(
        code='low-top-score',
        severity='medium',
        pattern='\\b(top_score|score)\\s*[:=]\\s*0\\.[01][0-9]\\b',
        message='top retrieval score appears weak',
        recommendation='Review chunking, query rewriting, or index freshness.',
    ),
    Rule(
        code='missing-source',
        severity='low',
        pattern='\\b(source\\s*[:=]\\s*(missing|none|null)|citation missing)\\b',
        message='source metadata is missing',
        recommendation='Persist source URI or document identifier with each hit.',
    ),
)
