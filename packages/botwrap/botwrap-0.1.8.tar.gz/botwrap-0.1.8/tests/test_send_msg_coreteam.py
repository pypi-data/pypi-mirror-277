# C:\Users\jamig\OneDrive\Desktop\botwrap\tests\test_send_msg_coreteam.py

from openaiwrapper.main import send_msg_coreteam
from openaiwrapper.profiles import load_coreteam_profile_1  # Replace with the desired core team profile loader

if __name__ == "__main__":
    send_msg_coreteam(load_coreteam_profile_1)
