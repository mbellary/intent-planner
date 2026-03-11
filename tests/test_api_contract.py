from fastapi.testclient import TestClient

from planner.api.app import app

client = TestClient(app)


def test_plan_endpoint_returns_enveloped_response():
    response = client.post(
        "/v1/plan",
        headers={"x-request-id": "req-1", "x-idempotency-key": "idem-1"},
        json={
            "intent_id": "intent_001",
            "kind": "ForexPredictionModel",
            "spec": {
                "dataset": "eurusd_hourly",
                "instrument": "EURUSD",
                "prediction_target": "volatility",
                "retrain_frequency": "weekly",
                "evaluation_metric": "sharpe_ratio",
            },
        },
    )

    payload = response.json()
    assert response.status_code == 200
    assert response.headers["x-request-id"] == "req-1"
    assert payload["api_version"] == "v1"
    assert payload["idempotency_key"] == "idem-1"
    assert payload["data"]["intent_id"] == "intent_001"
