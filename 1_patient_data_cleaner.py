#!/usr/bin/env python3
"""
Patient Data Cleaner

This script standardizes and filters patient records according to specific rules:

Data Cleaning Rules:
1. Names: Capitalize each word (e.g., "john smith" -> "John Smith")
2. Ages: Convert to integers, set invalid ages to 0
3. Filter: Remove patients under 18 years old
4. Remove any duplicate records

Input JSON format:
    [
        {
            "name": "john smith",
            "age": "32",
            "gender": "male",
            "diagnosis": "hypertension"
        },
        ...
    ]

Output:
- Cleaned list of patient dictionaries
- Each patient should have:
  * Properly capitalized name
  * Integer age (≥ 18)
  * Original gender and diagnosis preserved
- No duplicate records
- Prints cleaned records to console

Example:
    Input: {"name": "john smith", "age": "32", "gender": "male", "diagnosis": "flu"}
    Output: {"name": "John Smith", "age": 32, "gender": "male", "diagnosis": "flu"}

Usage:
    python patient_data_cleaner.py
"""

import json
import os
import pandas as pd


def load_patient_data(filepath):
    """
    Load patient data from a JSON file.
    
    Args:
        filepath (str): Path to the JSON file
        
    Returns:
        list: List of patient dictionaries
    """
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        # BUG: No error handling for file not found
        # FIX: Added exception handling for missing file
        print(f"Error: File not found: {filepath}")
        return []

def clean_patient_data(patients):
    """
    Clean patient data by:
    - Capitalizing names
    - Converting ages to integers
    - Filtering out patients under 18
    - Removing duplicates
    
    Args:
        patients (list): List of patient dictionaries
        
    Returns:
        list: Cleaned list of patient dictionaries
    """
    cleaned_patients = []
    for patient in patients:
        # BUG: Typo in key 'nage' instead of 'name'
        # FIX: Corrected to 'name'
        patient['name'] = patient['name'].title()

        try:
            # BUG: Wrong method name (fill_na vs fillna)
            # FIX: Convert age to int safely
            patient['age'] = int(patient['age'])
        except (ValueError, TypeError):
            # FIX: Set invalid ages to 0
            patient['age'] = 0

        # BUG: Wrong comparison operator (= vs ==)
        # BUG: Logic error - keeps underage patients instead of filtering them out
        # FIX: Keep only patients age 18 and above
        if patient['age'] >= 18:
            cleaned_patients.append(patient)

    # BUG: Wrong method name (drop_duplcates vs drop_duplicates)
    # FIX: Use dict-based deduplication inline here
    unique_patients = []
    for p in cleaned_patients:
        if p not in unique_patients:
            unique_patients.append(p)

    # BUG: Missing return statement for empty list
    # FIX: Update return lines to 'list empty' if empty
    if not cleaned_patients:
        print("List empty")
    
    return unique_patients

def main():
    """Main function to run the script."""
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the path to the data file
    data_path = os.path.join(script_dir, 'data', 'raw', 'patients.json')
    
    patients = load_patient_data(data_path)

    # Clean the patient data
    cleaned_patients = clean_patient_data(patients)
    
    # BUG: No error handling for load_patient_data failure
    # BUG: No check if cleaned_patients is None
    # FIX: Added check to handle empty or missing data
    if not cleaned_patients:
        print("No valid patient data to display.")
        return
    
    # Print the cleaned patient data
    print("Cleaned Patient Data:")
    for patient in cleaned_patients:
        # BUG: Using 'name' key but we changed it to 'nage'
        print(f"Name: {patient['name']}, Age: {patient['age']}, Diagnosis: {patient['diagnosis']}")
    
    # Return the cleaned data (useful for testing)
    return cleaned_patients

if __name__ == "__main__":
    main()