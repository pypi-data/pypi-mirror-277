from sceptr import variant
from numpy import ndarray
from pandas import DataFrame


default_model = variant.default()


def calc_cdist_matrix(anchors: DataFrame, comparisons: DataFrame) -> ndarray:
    return default_model.calc_cdist_matrix(anchors, comparisons)


def calc_pdist_vector(instances: DataFrame) -> ndarray:
    return default_model.calc_pdist_vector(instances)


def calc_vector_representations(instances: DataFrame) -> ndarray:
    return default_model.calc_vector_representations(instances)
