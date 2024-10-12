from LightningDetector import LightningDetector
import os
import argparse

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Process videos to detect lightning flashes")
    parser.add_argument("folder_path", help="Path to the folder containing the videos")
    args = parser.parse_args()

    # Check if the provided folder path exists
    if not os.path.isdir(args.folder_path):
        print(f"Error: The folder '{args.folder_path}' does not exist.")
        return

    # Create an instance of LightningDetector
    detector = LightningDetector()

    # Process the videos in the specified folder
    detector.process_videos(args.folder_path)

if __name__ == "__main__":
    main()