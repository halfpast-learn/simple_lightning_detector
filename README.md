# Lightning Flash Detector

This project is designed to process video files, detect lightning flashes, and create a compilation video of the detected flashes. It's useful for meteorologists, storm chasers, or anyone interested in analyzing lightning activity in video recordings.

## Components

The project consists of two main Python files and a Jupyter notebook:

1. `app/LightningDetector.py`: Contains the `LightningDetector` class, which handles the core functionality of detecting lightning flashes and processing videos.
2. `app/main.py`: The entry point of the application, which uses the `LightningDetector` class to process videos in a specified folder.
3. `notebooks/detector.ipynb`: A Jupyter notebook that also includes the `LightningDetector` class and provides example usage. This notebook is useful for interactive exploration and testing of the lightning detection functionality.

## Features

- Analyzes video files to detect sudden increases in brightness, which are likely to be lightning flashes.
- Creates a plot of frame brightness over time for each video, showing detected flashes.
- Cuts and compiles segments of the video where lightning flashes are detected.
- Merges all compiled videos into a single final video.

## Requirements

- Python 3.6+
- OpenCV (cv2)
- NumPy
- Matplotlib
- tqdm

## Installation

1. Clone this repository:   ```
   git clone https://github.com/halfpast-learn/simple_lightning_detector.git
   cd simple-lightning-detector   ```

2. Install the required packages:   ```
   pip install -r requirements.txt   ```

## Usage

1. Ensure you're in the project directory:   ```
   cd app   ```

2. Run the script, specifying the folder containing your video files:   ```
   python main.py /path/to/your/video/folder   ```

3. The script will process all `.mp4` files in the specified folder. For each video, it will:
   - Detect lightning flashes
   - Create a brightness plot
   - Cut and compile segments with detected flashes

4. After processing all videos, it will merge the compiled segments into a single video named `final_combined_video.mp4` in the same folder.

## Output

- Brightness plots for each video
- Individual compiled videos for each input video (named `clips_<original_filename>.mp4`)
- A final merged video of all detected flashes (`merged_clips.mp4`)

## Customization

You can modify the detection parameters in the `LightningDetector` class to adjust sensitivity or change the duration of video clips around each detected flash.

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check [issues page](https://github.com/halfpast-learn/simple_lightning_detector/issues) if you want to contribute.

## License

[MIT](https://choosealicense.com/licenses/mit/)
