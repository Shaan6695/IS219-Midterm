"""
Tests for the csv files
"""

import os
import pandas as pd
from main import save_history_to_csv, load_history_from_csv


# Define save_history_to_csv to accept history and directory path
def save_history_to_csv(history, directory_path):
    """Save history to CSV."""
    csv_file = os.path.join(directory_path, 'calculation_history.csv')
    df = pd.DataFrame({'Calculation': history})
    df.to_csv(csv_file, index=False)

# Define load_history_from_csv to accept directory path
def load_history_from_csv(directory_path):
    """Load history from CSV."""
    csv_file = os.path.join(directory_path, 'calculation_history.csv')
    if os.path.exists(csv_file):
        df = pd.read_csv(csv_file)
        return df['Calculation'].tolist()
    return []

# Test save_history_to_csv function
def test_save_history_to_csv(tmp_path):
    """Test save_history_to_csv function."""
    # Create a temporary directory for testing
    test_dir = tmp_path / "data"
    test_dir.mkdir()
    # Generate sample history
    history = ['calculation1', 'calculation2', 'calculation3']
    # Call the function to save history to CSV
    save_history_to_csv(history, test_dir)  # Pass the directory object
    # Check if the CSV file is created
    csv_file = test_dir / 'calculation_history.csv'
    assert csv_file.exists()
    # Check if the saved CSV file contains the correct data
    df = pd.read_csv(csv_file)
    assert df['Calculation'].tolist() == history

# Test load_history_from_csv function
def test_load_history_from_csv(tmp_path):
    """Test load_history_from_csv function."""
    # Create a temporary directory for testing
    test_dir = tmp_path / "data"
    test_dir.mkdir()
    # Create a sample CSV file with history
    csv_file = test_dir / 'calculation_history.csv'
    df = pd.DataFrame({'Calculation': ['calculation1', 'calculation2', 'calculation3']})
    df.to_csv(csv_file, index=False)
    # Call the function to load history from CSV
    loaded_history = load_history_from_csv(test_dir)  # Pass the directory object
    # Check if the loaded history matches the expected data
    expected_history = ['calculation1', 'calculation2', 'calculation3']
    assert loaded_history == expected_history
