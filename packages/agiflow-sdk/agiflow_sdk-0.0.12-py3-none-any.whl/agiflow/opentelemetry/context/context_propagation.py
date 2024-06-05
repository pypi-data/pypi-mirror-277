from typing import Any
import base64
import json
from opentelemetry.trace.propagation.tracecontext import TraceContextTextMapPropagator
from opentelemetry.context import get_current, set_value
from agiflow.opentelemetry.context.constants import ContextKeys


def get_carrier_from_trace_context():
    carrier = {}
    context = get_current()
    TraceContextTextMapPropagator().inject(carrier)
    carrier[ContextKeys.ASSOCIATION_PROPERTIES] = context.get(ContextKeys.ASSOCIATION_PROPERTIES, {})
    carrier[ContextKeys.PROMPT_SETTINGS] = context.get(ContextKeys.PROMPT_SETTINGS, {})
    carrier[ContextKeys.WORKFLOW_NAME] = context.get(ContextKeys.WORKFLOW_NAME, {})
    carrier[ContextKeys.OVERRIDE_ENABLE_CONTENT_TRACING] = context.get(ContextKeys.OVERRIDE_ENABLE_CONTENT_TRACING, {})
    return carrier


def get_trace_context_from_carrier(carrier):
    ctx = TraceContextTextMapPropagator().extract(carrier)
    if carrier is not None:
        if carrier.get(ContextKeys.ASSOCIATION_PROPERTIES):
            ctx = set_value(ContextKeys.ASSOCIATION_PROPERTIES, carrier.get(ContextKeys.ASSOCIATION_PROPERTIES), ctx)
        if carrier.get(ContextKeys.PROMPT_SETTINGS):
            ctx = set_value(ContextKeys.PROMPT_SETTINGS, carrier.get(ContextKeys.PROMPT_SETTINGS), ctx)
        if carrier.get(ContextKeys.WORKFLOW_NAME):
            ctx = set_value(ContextKeys.WORKFLOW_NAME, carrier.get(ContextKeys.WORKFLOW_NAME), ctx)
        if carrier.get(ContextKeys.OVERRIDE_ENABLE_CONTENT_TRACING):
            ctx = set_value(
              ContextKeys.OVERRIDE_ENABLE_CONTENT_TRACING,
              carrier.get(ContextKeys.OVERRIDE_ENABLE_CONTENT_TRACING),
              ctx
            )
    return ctx


def extract_association_properties_from_http_headers(headers: Any):
    if hasattr(headers, 'get'):
        association_properties = {}
        # old method to get trace as string
        action_id = headers.get('x-agiflow-action-id')
        # New method to get trace as base64 encoding json
        trace_id = headers.get('x-agiflow-trace-id')
        auto_trace = headers.get('x-agiflow-auto-trace')
        task_id = None
        task_name = None
        session_id = None

        if trace_id is not None:
            trace_string = base64.b64decode(trace_id)
            trace_obj = json.loads(trace_string)

            if trace_obj is not None:
                if trace_obj.get('id'):
                    action_id = trace_obj.get('id')
                if trace_obj.get('task_id'):
                    task_id = trace_obj.get('task_id')
                if trace_obj.get('task_name'):
                    task_name = trace_obj.get('task_name')
                if trace_obj.get('session_id'):
                    session_id = trace_obj.get('session_id')

        if action_id is not None:
            association_properties['action_id'] = action_id

        if task_id is not None:
            association_properties['task_id'] = task_id

        if task_name is not None:
            association_properties['task_name'] = task_name

        if session_id is not None:
            association_properties['session_id'] = session_id

        if auto_trace is not None and auto_trace.lower() == 'true':
            association_properties['auto_trace'] = True
