from functools import partial
import numpy as np


def _as_categories(x_multinomial):
    """Convert multinomial sample to long vector of categorical draws."""
    #  Line up all draws in one long vector (of size `n_samples`), indicating which
    # feature was drawn.
    # Use Numpy instead of JAX implementation because it is faster.
    return np.repeat(np.arange(len(x_multinomial)), x_multinomial)  # type: ignore


def _as_multinomial(x_categorical, n_features: int):
    """Convert string of categorical draws to multinomial representation."""
    x_test = np.zeros(n_features)
    np.add.at(x_test, x_categorical, 1)  # In place change.
    return x_test  # type: ignore


def _single_multinomial_train_test_split(
    random_state, x_i, test_size: float = 0.2
) -> tuple:
    """Make train-test split for a single multinomial draw.

    Args:
        random_state: Instance of NumPy pseudo random number state.
        x_i: A single multinomial observation.
        test_size: Proportion of draws for test set.
    """
    x_i = x_i.astype(int)
    x_draws = _as_categories(x_i)
    # Take, on average, `n_test` draws from test set (i.e., without replacement).
    u = random_state.uniform(size=len(x_draws))
    selected = u <= test_size
    x_test_draws = x_draws[selected]
    # Go back to multinomial representation.
    x_test = _as_multinomial(x_test_draws, n_features=len(x_i))  # type: ignore
    # Remainder is train set.
    x_train = x_i - x_test
    return x_train, x_test


def holdout_split(X, test_size=0.5, random_state=None):
    """Make train-test split from of a dataset of multinomial draws.

    Args:
        X: A dataset of multinomial observations, with independent samples along the
            rows.
        test_size: Proportion of draws to reserve for the test set.
        random_state: Seed for numpy pseudo random number generator state.

    Returns:
        A pair `X_train`, `X_test` both with same shape as `X`.
    """
    random_state = np.random.default_rng(random_state)

    _single_split = partial(_single_multinomial_train_test_split, test_size=test_size)
    x_as = []
    x_bs = []
    for x_i in X:
        x_a, x_b = _single_split(random_state, x_i)
        x_as.append(x_a)
        x_bs.append(x_b)
    return np.stack(x_as), np.stack(x_bs)
