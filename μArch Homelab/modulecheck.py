import subprocess
import sys

def ensure_modules(modules):
    builtin_modules = {"tkinter", "os", "time", "webbrowser"}
    install_map = {"PIL": "Pillow"}

    for module in modules:
        if module in builtin_modules:
            continue

        package = install_map.get(module, module)
        try:
            __import__(module)
        except ImportError:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# List of required modules
REQUIRED_MODULES = ["PIL"]

# Ensure modules are installed
ensure_modules(REQUIRED_MODULES)

# Import the modules
import tkinter as tk
from tkinter import messagebox
import os
import time
import webbrowser
from PIL import Image, ImageTk
