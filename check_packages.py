import importlib

modules = [
    'os',
    'sys',
    'cv2',
    'rclpy',
    'getopt',
    'subprocess',
    'rclpy.node',
    'cv_bridge',
    'sensor_msgs.msg',
    'theora_image_transport.msg',
    'ros2bag.api',
    'ros2cli.node',
    'argparse'
]

for module in modules:
    try:
        importlib.import_module(module)
        print(f"Module '{module}' is installed.")
    except ImportError:
        print(f"Module '{module}' is NOT installed.")