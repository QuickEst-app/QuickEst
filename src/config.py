"""
Module Constants

This module defines several constants used throughout the application, including database operation statuses, file extensions, and resource paths.
"""

# Database Constants
ALREADY_EXIST = -1
FAILURE = -2
NOT_EXIST = 0
SUCCESS = 1
TOO_MANY_PROJECTS = -3

# Limits
ACTOR_LIMIT = 200
PROJECT_LIMIT = 500
TOTAL_EFFORT = 20000
USE_CASE_LIMIT = 1000

# File Constants
FILE_EXTENSION = ".qck"
PROJECT_FILE_EXTENSION = ".qckproj"

ACTORS_FILE = f"actors{FILE_EXTENSION}"
ENVIRONMENTAL_FACTORS_FILE = f"environmental_factors{FILE_EXTENSION}"
PARAMETERS_FILE = f"parameters{FILE_EXTENSION}"
PROJECT_FILE = f"project{FILE_EXTENSION}"
TECHNICAL_FACTORS_FILE = f"technical_factors{FILE_EXTENSION}"
USE_CASES_FILE = f"use_cases{FILE_EXTENSION}"

# Resources
FILES_PATH = ":/resources/files/"
FONTS_PATH = ":/resources/fonts/"
IMAGES_PATH = ":/resources/images/"

# Files
CONTENTS_FILE = f"{FILES_PATH}contents.pdf"
LICENSE_FILE = f"{FILES_PATH}LICENSE.pdf"

# Fonts
TITLE_FONT = f"{FONTS_PATH}Audiowide-Regular.ttf"

# Images
CANCEL_DISABLED_IMG = f"{IMAGES_PATH}cancelDisabled.png"
CANCEL_FACTORS_IMG = f"{IMAGES_PATH}cancel.png"
CLEAR_SEARCH_IMG = f"{IMAGES_PATH}clearSearch.png"
COMMENT_IMG_GREEN = f"{IMAGES_PATH}greenComment.png"
COMMENT_IMG_BLUE = f"{IMAGES_PATH}blueComment.png"
COMMENT_IMG_YELLOW = f"{IMAGES_PATH}yellowComment.png"
CONFIRMATION_IMG = f"{IMAGES_PATH}question.png"
CRITICAL_IMG = f"{IMAGES_PATH}critical.png"
DELETE_DISABLED_IMG = f"{IMAGES_PATH}deleteDisabled.png"
DELETE_IMG = f"{IMAGES_PATH}delete.png"
DELETE_PROJECT_IMG = f"{IMAGES_PATH}deleteProject.png"
DOWNLOAD_PROJECT_IMG = f"{IMAGES_PATH}downloadProject.png"
EDIT_DISABLED_IMG = f"{IMAGES_PATH}editDisabled.png"
EDIT_IMG = f"{IMAGES_PATH}edit.png"
EDIT_PROJECT_IMG = f"{IMAGES_PATH}editProject.png"
EXCEL_IMG =  f"{IMAGES_PATH}excel.png"
FAVORITE_IMG = f"{IMAGES_PATH}favorite.png"
INFO_IMG_BLUE = f"{IMAGES_PATH}info_blue.png"
INFO_IMG_GREEN = f"{IMAGES_PATH}info_green.png"
INFORMATION_IMG = f"{IMAGES_PATH}information.png"
LICENSE_IMG = f"{IMAGES_PATH}LGPLv3.png"
NEW_DISABLED_IMG = f"{IMAGES_PATH}new_disabled.png"
NEW_IMG = f"{IMAGES_PATH}new.png"
NEW_PROJECT_IMG = f"{IMAGES_PATH}newProject.png"
NOT_FAVORITE_IMG = f"{IMAGES_PATH}notFavorite.png"
PROJECT_OPTIONS_IMG = f"{IMAGES_PATH}projectOptions.png"
QUICKEST_IMG = f"{IMAGES_PATH}quickest.png"
SAVE_DISABLED_IMG= f"{IMAGES_PATH}saveDisabled.png"
SAVE_FACTORS_IMG = f"{IMAGES_PATH}saveFactors.png"
SAVE_IMG = f"{IMAGES_PATH}save.png"
SEARCH_IMG = f"{IMAGES_PATH}search.png"
WARNING_IMG = f"{IMAGES_PATH}warning.png"
