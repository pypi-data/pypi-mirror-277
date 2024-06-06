# Path: C:\Users\jamig\OneDrive\Desktop\botwrap\openaiwrapper\profiles.py

from openaiwrapper.decorators import log_function_call
import os
import json

@log_function_call
def load_coreteam_profile_1():
    """Load the profile for Brie."""
    profile_path = os.path.join(os.path.dirname(__file__), "profiles", "coreteam_brie.json")

    if not os.path.exists(profile_path):
        raise ValueError(f"Profile file '{profile_path}' not found")

    with open(profile_path, "r") as file:
        profile = json.load(file)

    return profile

@log_function_call
def load_coreteam_profile_2():
    """Load the profile for Britt."""
    profile = {
        "name": "Britt",
        "instructions": "You are Britt, a Business Strategist and Computer Science Enthusiast. Help with business strategy and project management.",
        "tools": [{"type": "code_interpreter"}],
        "model": "gpt-4-1106-preview"
    }
    return profile

@log_function_call
def load_coreteam_profile_3():
    """Load the profile for Derek."""
    profile = {
        "name": "Derek",
        "instructions": "You are Derek, an Innovative CEO and Engineering Economist. Provide strategic business insights and leadership.",
        "tools": [{"type": "code_interpreter"}],
        "model": "gpt-4-1106-preview"
    }
    return profile

@log_function_call
def load_coreteam_profile_4():
    """Load the profile for Max."""
    profile = {
        "name": "Max",
        "instructions": "You are Max, a Strategy Analyst and Critical Thinker. Offer analytical perspectives and strategic planning.",
        "tools": [{"type": "code_interpreter"}],
        "model": "gpt-4-1106-preview"
    }
    return profile

@log_function_call
def load_coreteam_profile_5():
    """Load the profile for Nate."""
    profile = {
        "name": "Nate",
        "instructions": "You are Nate, a Software Engineer and Gaming Enthusiast. Develop software solutions and stay updated with gaming trends.",
        "tools": [{"type": "code_interpreter"}],
        "model": "gpt-4-1106-preview"
    }
    return profile

@log_function_call
def load_coreteam_profile_6():
    """Load the profile for Riley."""
    profile = {
        "name": "Riley",
        "instructions": "You are Riley, an AI Expert, Prompt Engineer & Project Manager. Integrate AI/ML with cognitive neuroscience principles and manage projects effectively.",
        "tools": [{"type": "code_interpreter"}],
        "model": "gpt-4-1106-preview"
    }
    return profile

@log_function_call
def load_non_coreteam_profile(profile_id):
    """Load a non-coreteam assistant profile from a JSON file."""
    profile_dir = os.path.join(os.path.dirname(__file__), "profiles")
    profile_path = os.path.join(profile_dir, f"{profile_id}.json")

    if not os.path.exists(profile_path):
        raise ValueError(f"Profile file '{profile_path}' not found")

    with open(profile_path, "r") as file:
        profile = json.load(file)

    return profile

