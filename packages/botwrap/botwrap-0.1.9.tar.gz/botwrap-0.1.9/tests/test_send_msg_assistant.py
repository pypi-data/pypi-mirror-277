from openaiwrapper.main import send_msg_coreteam
from openaiwrapper.profiles import load_non_coreteam_profile

if __name__ == "__main__":
    profile_id = "example_non_coreteam_profile"  # Replace with the actual profile ID (file name without .json)
    send_msg_coreteam(lambda: load_non_coreteam_profile(profile_id))
