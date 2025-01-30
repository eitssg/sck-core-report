"""Lambda handler to inspect Task Payload and return a result"""

import core_logging as log

from core_framework.models import TaskPayload

from core_report import __version__


def handler(event: dict, context: dict | None) -> str:
    """
    Tool to inspect result from stepfunction exe4cution.

    Expects event to be created by TaskPayload model.

    task_payload = TaskPayload(**details)

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
    log.trace("Report instection received event: {}".format(event))

    try:
        try:
            task_payload = TaskPayload(**event)
        except Exception as e:
            raise Exception("Invalid task payload: {}".format(e))

        log.info("Task Payload Inspecter v{}", __version__)
        log.info(
            "Inspection of task payload task: {}, flow_control: {}".format(
                task_payload.Task, task_payload.FlowControl
            )
        )

        log.debug("Task Payload:", details=task_payload.model_dump())

        fc = task_payload.FlowControl

        if fc == "success":
            return "SUCCESS"

        if fc == "failure":
            raise Exception("A failure occurred. See logs for further details.")

        raise Exception(
            "Unknown failure condition occurred (flow_control = '{}'). "
            "See logs for further details.".format(fc)
        )
    finally:
        log.trace("Report inspection complete")
