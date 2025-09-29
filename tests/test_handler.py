import pytest
import json

import core_framework as util

from core_framework.models import (
    TaskPayload,
    DeploymentDetails as DeploymentDetailsClass,
)

from core_report.main import handler
from core_execute import load_state, save_state

client = util.get_client() or "core"


@pytest.fixture(scope="module")
def task_payload() -> TaskPayload:

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

    state = {"flow_control": "failure"}

    save_state(task_payload, state)

    event = task_payload.model_dump()

    response = handler(event, None)

    assert isinstance(response, dict)
    assert response["statusCode"] == 200
    assert response["body"] == json.dumps(state)

    loaded_state = load_state(task_payload)

    assert loaded_state.get("flow_control") == "failure"


def test_report_success(task_payload: TaskPayload):

    state = {"flow_control": "success"}

    save_state(task_payload, state)

    event = task_payload.model_dump()

    response = handler(event, None)

    assert isinstance(response, dict)
    assert response["statusCode"] == 200
    assert response["body"] == json.dumps(state)

    loaded_state = load_state(task_payload)

    assert loaded_state.get("flow_control") == "success"


def test_report_other(task_payload: TaskPayload):

    state = {"flow_control": "pending"}

    save_state(task_payload, state)

    response = handler(task_payload.model_dump(), None)

    assert isinstance(response, dict)
    assert response["statusCode"] == 200
    assert response["body"] == json.dumps(state)


def test_invalid_payload():

    response = handler({}, None)

    assert isinstance(response, dict)
    assert response["statusCode"] == 500

    print(json.loads(response["body"]))
