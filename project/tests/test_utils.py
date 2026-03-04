import pytest
import numpy as np
from project import utils


class DummyScaler:
    def transform(self, x):
        return np.array([[0.5]])

class DummyEncoder:
    def transform(self, x):
        return np.array([[1, 0]])

class DummyModel:
    def predict(self, x):
        return np.array([1])

    def predict_proba(self, x):
        return np.array([[0.2, 0.8]])


# -------------------------
# Auto Mock All Artifacts
# -------------------------

@pytest.fixture(autouse=True)
def mock_artifacts(monkeypatch):
    monkeypatch.setattr(utils, "_bmi_sc", DummyScaler(), raising=False)
    monkeypatch.setattr(utils, "_ss_ohe", DummyEncoder(), raising=False)
    monkeypatch.setattr(utils, "_allergies_ohe", DummyEncoder(), raising=False)
    monkeypatch.setattr(utils, "_apl_ohe", DummyEncoder(), raising=False)
    monkeypatch.setattr(utils, "_pal_ohe", DummyEncoder(), raising=False)
    monkeypatch.setattr(utils, "_logit_model", DummyModel(), raising=False)


# -------------------------
# Test Cases
# -------------------------

def test_asthma_prediction_valid():
    pred, prob = utils.asthma_prediction(
        BMI=22,
        Family_History=1,
        Smoking_Status='Never',
        Allergies='Dust',
        Air_Pollution_Level='Moderate',
        Physical_Activity_Level='Moderate'
    )

    assert pred in [0, 1]
    assert isinstance(prob, float) or isinstance(prob, np.float64)
    assert 0 <= prob <= 1


def test_invalid_family_history_type():
    with pytest.raises(Exception):
        utils.asthma_prediction(
            BMI=22,
            Family_History="Yes",  # invalid type
            Smoking_Status='Never',
            Allergies='Dust',
            Air_Pollution_Level='Moderate',
            Physical_Activity_Level='Moderate'
        )


def test_boundary_bmi_value():
    pred, prob = utils.asthma_prediction(
        BMI=0,  # edge case
        Family_History=0,
        Smoking_Status='Never',
        Allergies='Dust',
        Air_Pollution_Level='Low',
        Physical_Activity_Level='High'
    )

    assert pred in [0, 1]
    assert 0 <= prob <= 1