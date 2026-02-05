"""
Central configuration for Automatic CSV Data Cleaner
Controls current application behavior.
"""

# ==============================
# Application Info
# ==============================
APP_NAME = "Automatic CSV Data Cleaner"

# ==============================
# Cleaning Settings (USED NOW)
# ==============================

# Duplicate handling
REMOVE_DUPLICATES = True

# Missing value handling
NUMERICAL_IMPUTE_STRATEGY = "median"      # currently used
CATEGORICAL_IMPUTE_STRATEGY = "mode"      # currently used

# String & column cleanup
STRIP_COLUMN_NAMES = True
STRIP_STRING_VALUES = True

# ==============================
# UI Settings (USED NOW)
# ==============================

DATAFRAME_PREVIEW_ROWS = 5