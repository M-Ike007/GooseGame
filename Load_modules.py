"""
READ ME:
    Load modules function to try all imports

DESCRIPTION:
    This function tries to import all the imports that are present in modules.
    Otherwise, it will raise an exception for import is not working.

PARAMETERS:
    No parameters present.

LIMITATIONS:
    - might not work if anaconda version is too old
    - might not work if pycharm version is too old

STRUCTURES:
    try-except-structure: to try imports and otherwise raise error.

OUTPUT:
    No output. Only if there is an import error.


"""


def load_modules():
    try:
        import sys
        import random
        import pygame
        import logging
        import tkinter as tk
        import tkinter.messagebox
        from PIL import Image, ImageTk
        import logging
        import re

    except ImportError as exc:
        sys.stderr.write(f"Error: failed to import package ({format(exc)})")
        sys.exit(2)

