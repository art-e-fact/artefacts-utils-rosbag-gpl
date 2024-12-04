# Artefacts-Utils Rosbag GPL package

Designed to be used with `artefacts-utils` this package contains code available under the GPL license.

## Standalone Usage

```
from artefacts_utils_rosbag_gpl.ros2bag2video import rosbag_to_mp4

rosbag_to_mp4(rosbag_filepath, topic_name, output_filepath, fps=20)
```

Will create an mp4 video from the images in a given camera topic from a provided rosbag (mcap or db3). The `rosbag_file_path` can be the path to the rosbag file itself, or the parent folder (containing the rosbag, and `metadata.yaml`)


With special thanks to @mlaiacker 's [ros2bag2video](https://github.com/mlaiacker/rosbag2video) which has been adapted here for ros2 video recordings.