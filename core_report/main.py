"""Lambda handler to inspect Task Payload and return a result"""

import core_logging as log
import json

from core_framework.models import TaskPayload
from core_execute import load_state


def get_module_version() -> str:
    # return the version of this packackage
    version = "1.0.0"
    return version


def handler(event: dict, context: dict | None) -> dict:
    """
    Tool to inspect result from stepfunction exe4cution.

    Expects event to be created by TaskPayload model.

    task_payload = TaskPayload.model_validate(details)

    event = task_payload.model_dump()

    Args:
        event (dict): The task payload
        context (dict): Lambda execution context

    Raises:
        Exception: if the event is not a valid task payload
        Exception: if FlowControl is 'failure'
        Exception: if FlowControl is not a valid value

    Returns:
        str: "SUCCESS" if FlowControl is 'success'
    """
    try:
        task_payload = TaskPayload.model_validate(event)

        log.info("Task Payload Inspecter v{}", get_module_version())
        log.info("Inspection of task payload task: {}, flow_control: {}".format(task_payload.task, task_payload.flow_control))

        log.debug("Task Payload:", details=task_payload.model_dump())

        state = load_state(task_payload)

        flow_control = state.get("flow_control", "unknown")

        body = {"flow_control": flow_control}

        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps(body),
        }

    except Exception as e:

        log.error("Error processing task payload: {}", str(e))

        return {
            "statusCode": 500,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({"error": str(e)}),
        }
