"""
gpu_metrics.py
"""
import subprocess
import json
from typing import Dict
from server_metrics.utils.parse_gpu_json import Gpu, parse_gpu_json_to_dict
from server_metrics.utils.write_gpu_prom import create_gpu_prom_file
from server_metrics.utils.xml_parser import xml_to_json

def run_nvidia_smi(ip: str, port: int, key_path: str, username: str):
    """
    Gets GPU data from servers using nvidia-smi

    Args:
        ip (str):
        port (int):
        key_path (str):
        username (str):
    """
    try:
        # Command to connect via SSH and run nvidia-smi
        ssh_command = [
            "ssh",
            "-i", key_path,
            "-p", str(port),
            f"{username}@{ip}",
            "nvidia-smi -q -x"
        ]

        # Execute the SSH command
        result = subprocess.run(ssh_command, capture_output=True, text=True, check=False)

        if result.stdout:
            json_output = json.dumps(xml_to_json(result.stdout), indent=4)
            json_data = json.loads(json_output)

            if "gpu" in json_data:
                gpu_dict: Dict[int, Gpu] = {}
                # Check the number of attached GPUs
                num_gpus = int(json_data["attached_gpus"]["text"])
                if num_gpus > 1:
                    gpus = json_data["gpu"]
                    for index, gpu in enumerate(gpus):
                        gpu_dict[index] = parse_gpu_json_to_dict(gpu)
                else:
                    gpu = json_data["gpu"]
                    gpu_dict[0] = parse_gpu_json_to_dict(gpu)

                create_gpu_prom_file(ip, port, gpu_dict)

            # file_path = f"output_{ip}_{port}.json"  # Define a unique file name
            # with open(file_path, 'w', encoding=str) as file:
            #     file.write(json_output)
            # print(f"JSON Output saved to {file_path}")
            # print(f"JSON Output from {ip}:{port}\n{json_output}")
        elif result.stderr:
            print(f"Errors from {ip}:{port}\n{result.stderr}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to execute on {ip}:{port}: {e}")
