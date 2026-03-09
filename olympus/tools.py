"""
OLYMPUS Tools — Tool registration for the OLYMPUS multi-agent system.
"""

import json
from typing import Any, Dict

from olympus.agents.hermes_orchestrator import route_to_gods
from tools.registry import registry

def olympus_orchestrate(args: Dict[str, Any], **kwargs) -> str:
    """
    Orchestrate a task via the OLYMPUS divine pantheon.
    Routes the message to the appropriate god(s) and returns the routing plan.
    """
    message = args.get("message", "")
    if not message:
        return json.dumps({"error": "No message provided to OLYMPUS"})
    
    plan = route_to_gods(message)
    return json.dumps({
        "status": "success",
        "message": f"⚡ OLYMPUS has received your request. {plan['rationale']}",
        "plan": plan
    }, ensure_ascii=False)

# Tool Schema
OLYMPUS_ORCHESTRATE_SCHEMA = {
    "name": "olympus_orchestrate",
    "description": "Invoke the OLYMPUS Second Brain. This tool uses the divine pantheon (Hermes, Perseus, Mnemosyne, Asclepius, Argus) to analyze, structure, and monitor your information. Use this for ANY request that involves memory capture, search, proactive insights, or reminders within the OLYMPUS ecosystem.",
    "parameters": {
        "type": "object",
        "properties": {
            "message": {
                "type": "string",
                "description": "The user's request or information to be processed by OLYMPUS."
            }
        },
        "required": ["message"]
    }
}

# Register the tool
registry.register(
    name="olympus_orchestrate",
    toolset="olympus",
    schema=OLYMPUS_ORCHESTRATE_SCHEMA,
    handler=olympus_orchestrate,
    description="Divine orchestration of tasks within the OLYMPUS Second Brain."
)
