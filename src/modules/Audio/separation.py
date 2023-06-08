"""Separate vocals from audio"""

import subprocess

from src.modules.console_colors import (
    ULTRASINGER_HEAD,
    blue_highlighted,
    red_highlighted,
)
from src.modules.os_helper import current_executor_path, move, path_join


def separate_audio(input_file_path: str, output_file: str, device="cpu") -> None:
    """Separate vocals from audio with demucs."""

    print(
        f"{ULTRASINGER_HEAD} Separating vocals from audio with {blue_highlighted('demucs')} and {red_highlighted(device)} as worker."
    )
    # Model selection?
    # -n mdx_q
    # -n htdemucs_ft
    device = "cpu" if device != "cuda" else "cuda"
    subprocess.run(
        ["demucs", "-d", device, "--two-stems=vocals", input_file_path]
    )
    separated_folder = path_join(current_executor_path(), "separated")
    move(separated_folder, output_file)