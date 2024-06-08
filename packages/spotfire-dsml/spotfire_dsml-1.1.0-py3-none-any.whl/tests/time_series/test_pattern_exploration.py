# test file for pattern_exploration:

#note full path.
import spotfire_dsml.time_series.pattern_exploration as mp
import pandas as pd
import pytest

@pytest.fixture
def test_data():
    data = pd.read_csv('./tests/time_series/pattern_exploration_data/test_data.csv')
    return data

@pytest.fixture
def test_index_data():
    data = pd.read_csv('./tests/time_series/pattern_exploration_data/test_index_data.csv')
    return data

@pytest.fixture
def test_mp_data():
    data = pd.read_csv('./tests/time_series/pattern_exploration_data/test_mp_data.csv')
    return data

def test_get_mp(test_data):
    result = mp.get_mp(test_data, 5000)
    assert isinstance(result, pd.DataFrame)
    assert result.shape == (52123, 5)

def test_get_motifs(test_mp_data):
    result = mp.get_motifs(test_mp_data)
    assert isinstance(result[0], pd.DataFrame)
    assert result[0].shape == (52123, 7)
    assert isinstance(result[1], pd.DataFrame)
    assert result[1].shape == (3, 4)
    assert isinstance(result[2], pd.DataFrame)
    assert result[2].shape == (5000, 2)

def test_display_motifs(test_index_data, test_data):
    result = mp.display_motifs(test_index_data, test_data)
    assert isinstance(result[0], pd.DataFrame)
    assert result[0].shape == (450, 3)
    assert isinstance(result[1], pd.Series)

# def test_display_motifs_with_fixtures(index_df_fixture, input_data_fixture, windowSize, request):
#     index_df = request.getfixturevalue(index_df_fixture)
#     input_data = request.getfixturevalue(input_data_fixture)
#     result = mp.display_motifs(index_df, input_data, windowSize)
