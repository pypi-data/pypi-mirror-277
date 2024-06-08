import pytest
import pandas as pd

@pytest.fixture(scope="module")
def test_data():
    return pd.read_csv('time_series/pattern_exploration_data/test_data.csv')


@pytest.fixture(scope="module")
def test_mp_data():
    return pd.read_csv('time_series/pattern_exploration_data/test_mp_data.csv')

@pytest.fixture(scope="module")
def test_display_motifs_data():
    return pd.read_csv('time_series/pattern_exploration_data/test_index_data.csv')

@pytest.fixture(scope="module")
def test_display_motifs_null_data():
    return pd.read_csv('time_series/pattern_exploration_data/test_index_data.csv').iloc[0:0]

@pytest.fixture(scope="module")
def test_mp_data_with_warnings():
    # Create test data that is likely to generate warnings
    data = {
        'mp': np.random.rand(100),
        'index': np.arange(100),
        'left_mp': np.random.rand(100),
        'right_mp': np.random.rand(100),
        'sequence': np.append(np.random.rand(95), [np.nan]*5)  # Include NaN values
    }
    return pd.DataFrame(data)
