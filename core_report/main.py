"""Lambda handler to inspect Task Payload and return a result"""

from core_framework.models import TaskPayload


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
    try:
        task_payload = TaskPayload(**event)
    except Exception as e:
        raise Exception("Invalid task payload: {}".format(e))

    fc = task_payload.FlowControl

    if fc == "success":
        return "SUCCESS"

    if fc == "failure":
        raise Exception("A failure occurred. See logs for further details.")

    raise Exception(
        "Unknown failure condition occurred (flow_control = '{}'). "
        "See logs for further details.".format(fc)
    )
