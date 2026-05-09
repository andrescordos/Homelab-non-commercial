import subprocess
import sys

def ensure_modules(modules):
    for module in modules:
        try:
            __import__(module)
        except ImportError:
            print(f"Installing {module}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", module])

# List of required modules
REQUIRED_MODULES = ["tkinter", "PIL", "webbrowser", "os", "time"]

# Ensure modules are installed
ensure_modules(REQUIRED_MODULES)

# Import the modules
import tkinter as tk
from tkinter import messagebox
import os
import time
import webbrowser
from PIL import Image, ImageTk
