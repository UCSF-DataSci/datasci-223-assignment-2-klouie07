# Summary

## Part 1: Patient Data Cleaning

**Script:** `1_patient_data_cleaner.py`

### Goal

Clean and standardize patient records by:

* Capitalizing patient names
* Converting age values to integers and defaulting invalid ages to 0
* Filtering out patients under 18 years old
* Removing duplicate patient records

### Bugs and Fixes

| Bug Description                                             | Fix Applied                                                             |
| ----------------------------------------------------------- | ----------------------------------------------------------------------- |
| Used incorrect key `'nage'` instead of `'name'`             | Replaced with `'name'` and capitalized using `.title()`                 |
| Attempted to call `.fill_na()` on an integer/string         | Replaced with a `try/except` to convert `age` to `int`, fallback to `0` |
| Used assignment `=` instead of comparison `>=` in age check | Changed to `if patient['age'] >= 18:`                                   |
| Returned `None` if list was empty                           | Changed to print `"List empty"` and return an empty list `[]`           |
| Printed `'name'` key that was no longer being set           | Corrected to print the properly formatted `'name'` key                  |

## Part 2: Emergency Room Medication Dosage Calculator

**Script:** `2_med_dosage_calculator.py`

### Bugs and Fixes

| Bug Description                                             | Fix Applied                                                                |
| ----------------------------------------------------------- | -------------------------------------------------------------------------- |
| Medication list `LOADING_DOSE_MEDICATIONS` missing commas   | Added missing commas to define valid list items                            |
| Appended `'s'` to medication name when accessing dictionary | Used correct medication name without modifying the key                     |
| Used `+` instead of `*` for dosage math                     | Replaced addition with multiplication                                      |
| Did not check for required keys in the patient dict         | Added checks                                                               |
| Incorrect medication names                                  | Fixed typos like `"epinephrin"` to `"epinephrine"`                         |
| No error handling on file load or missing data              | Added check around file loading                                            |

## Part 3: Cohort Analysis with Polars

**Script:** `3_cohort_analysis.py`

### Debugging and Adjustments

| Issue                                                       | Resolution                                             |
| ----------------------------------------------------------- | ------------------------------------------------------ |
| Error in `.cut()`                                           | Ensured `len(labels) == len(breaks) - 1`               |
| Attempted to use `.enable_streaming_engine()`               | Removed as it's no longer supported in recent versions |
| Streaming error                                             | Removed `streaming=True`, used `.collect()`            |

### Output Format 

```
bmi_range    avg_glucose    patient_count    avg_age
-----------------------------------------------------
Obese           148.0             1             50.0
Overweight       85.0             1             31.0
Normal          183.0             1             32.0
```

