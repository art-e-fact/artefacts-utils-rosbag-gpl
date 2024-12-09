# Artefacts Toolkit Rosbag GPL package

## Standalone Usage

```
from artefacts_toolkit_rosbag_gpl import extract_video

extract_video(rosbag_filepath, topic_name, output_filepath, fps=20)
```

Will create an mp4 video from the images in a given camera topic from a provided rosbag (mcap or db3). The `rosbag_file_path` can be the path to the rosbag file itself, or the parent folder (containing the rosbag, and `metadata.yaml`)


With special thanks to @mlaiacker 's [ros2bag2video](https://github.com/mlaiacker/rosbag2video) which has been adapted here for ros2 video recordings.