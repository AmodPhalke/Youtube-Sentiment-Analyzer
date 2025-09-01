import os
import pandas as pd
import pytest

from config import settings
from pages.youtube_page import *

@pytest.fixture(scope="module")
def youtube_page():
    yt = YoutubePage(settings.driver)
    yt.load_page()
    return yt

def test_youtube_comments_returns_dataframe(youtube_page):
    df = youtube_page.youtube_comments(settings.driver)

    # Check that return type is DataFrame
    assert isinstance(df, pd.DataFrame)

    # Check required columns exist
    for col in ["name", "comment", "likes"]:
        assert col in df.columns

    # Ensure dataframe is not empty
    assert not df.empty

def test_csv_file_created():
    # Ensure CSV file is created at expected location
    assert os.path.exists(settings.OUTPUT_CSV)

    # Ensure CSV is not empty
    df = pd.read_csv(settings.OUTPUT_CSV)
    assert not df.empty
