import numpy
from scipy.stats import entropy


class Selector:
    """Selects instances of low confidence for the given model, sampling from the given `pool` of instances. """
    def __init__(self, model):
        self.model = model

    def __call__(self, data: numpy.ndarray, k: int = 100):
        model_predictions = self.model.predict_proba(data)
        predictions_entropy = entropy(model_predictions, axis=1)

        top_predictions = numpy.argpartition(predictions_entropy, -k)[-k:]  # top-k

        return top_predictions
