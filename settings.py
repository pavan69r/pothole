from pathlib import Path
import sys


# Get the absolute path
file_path = Path(__file__).resolve()

# Get the parent directory
root_path = file_path.parent

# Add the root path
if root_path not in sys.path:
    sys.path.append(str(root_path))
#Current directory root
ROOT = root_path.relative_to(Path.cwd())

# Source selection Settings
VIDEO = 'Video'
STREAM = 'Stream'
SOURCES_LIST = [STREAM, VIDEO]

# Videos config
VIDEO_LIST = ['video 1', 'video 2', 'video 3', 'video 4', 'video 5']
VIDEO_DIR = ROOT / 'videoIN'
VIDEO_1_PATH = VIDEO_DIR / 'video_1.mp4'
VIDEO_2_PATH = VIDEO_DIR / 'video_2.mp4'
VIDEO_3_PATH = VIDEO_DIR / 'video_3.mp4'
VIDEO_4_PATH = VIDEO_DIR / 'video_4.mp4'
VIDEO_5_PATH = VIDEO_DIR / 'video_5.mp4'
VIDEOS_DICT = {
    'video 1': VIDEO_1_PATH,
    'video 2': VIDEO_2_PATH,
    'video 3': VIDEO_3_PATH,
    'video 4': VIDEO_4_PATH,
    'video 5': VIDEO_5_PATH,
}

#ML model settings
MODEL_DIR = ROOT / 'weights'
SEGMENTATION_MODEL = MODEL_DIR / 'best.pt' #'test1.pt' #OR 'yolov8s-seg.pt'