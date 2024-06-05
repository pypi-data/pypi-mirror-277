from pyod.models.suod import SUOD
from pyod.models.lof import LOF
from pyod.models.iforest import IForest
from pyod.models.copod import COPOD
from pyod.utils import generate_data

from unquad.enums.adjustment import Adjustment
from unquad.estimator.conformal import ConformalEstimator
from unquad.enums.method import Method
from unquad.evaluation.metrics import false_discovery_rate, statistical_power

if __name__ == "__main__":

    x_train, x_test, y_train, y_test = generate_data(
        n_train=1_000,
        n_test=1_000,
        n_features=10,
        contamination=0.1,
        random_state=1,
    )

    x_train = x_train[y_train == 0]

    detector_list = [
        LOF(n_neighbors=15),
        LOF(n_neighbors=20),
        LOF(n_neighbors=25),
        LOF(n_neighbors=35),
        COPOD(),
        IForest(n_estimators=100),
        IForest(n_estimators=200),
    ]

    ce = ConformalEstimator(
        detector=SUOD(
            base_estimators=detector_list, combination="average", verbose=False
        ),
        method=Method.CV,
        adjustment=Adjustment.BENJAMINI_HOCHBERG,
        alpha=0.1,
        random_state=2,
        split=10,
    )

    ce.fit(x_train)
    estimates = ce.predict(x_test, raw=False)

    print(false_discovery_rate(y=y_test, y_hat=estimates))
    print(statistical_power(y=y_test, y_hat=estimates))
