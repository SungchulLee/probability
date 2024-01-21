import os
import subprocess

def download_poker_card_images():
    repository_url = "https://github.com/georgemcredmond/BlackJackPython"
    destination_path = "./BlackJackPython"  # Replace with the desired destination path

    if os.path.exists(destination_path):
        print(f"Repository cloned already to {destination_path}")
        return
    
    # Run the git clone command
    try:
        subprocess.run(["git", "clone", repository_url, destination_path], check=True)
        print(f"Repository cloned successfully to {destination_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error cloning repository: {e}")

