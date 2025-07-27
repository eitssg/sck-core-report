import pytest
import os

from core_framework.models import (
    TaskPayload,
    DeploymentDetails as DeploymentDetailsClass,
)

from core_report.main import handler


@pytest.fixture(scope="module")
def task_payload():

    os.environ["CLIENT"] = "my-client"

    return TaskPayload(
        Task="deploy",
        DeploymentDetails=DeploymentDetailsClass(
            Portfolio="my-portfolio",
            App="my-app",
            Branch="my-dev-branch",
            Build="v1.0.0",
        ),
    )


def test_report_failure(task_payload: TaskPayload):

    try:
        task_payload.flow_control = "failure"

        response = handler(task_payload.model_dump(), None)

        assert False, response

    except Exception as e:
        assert str(e) == "A failure occurred. See logs for further details."


def test_report_success(task_payload: TaskPayload):

    try:
        task_payload.flow_control = "success"

        response = handler(task_payload.model_dump(), None)

        assert response == "SUCCESS"

    except Exception as e:
        assert False, str(e)


def test_report_other(task_payload: TaskPayload):

    try:
        task_payload.flow_control = "wait"

        response = handler(task_payload.model_dump(), None)

        assert False, response

    except Exception as e:

        assert (
            str(e) == "Unknown failure condition occurred ("
            "flow_control = 'wait'). See logs for further details."
        )


def test_invalid_payload():

    try:
        response = handler({}, None)

        assert False, response

    except Exception as e:

        assert "Invalid task payload" in str(e)
