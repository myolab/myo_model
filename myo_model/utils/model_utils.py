"""
Copyright (c) 2026 MyoLab, Inc.
Released under the MyoLab Non-Commercial Scientific Research License
on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
either express or implied.

You may not use this file except in compliance with the License.
See the LICENSE file for governing permissions and limitations.
"""

# Summary: Utility functions for retrieving model, asset and markerset paths

import os

curr_dir = os.path.dirname(os.path.realpath(__file__))


def get_model_xml_path(model_name=None):
    """Get the path to the model xml file.

    Args:
        model_name (str, optional): Name of the model file. If None, returns default myoskeleton.xml.

    Returns:
        str: Path to the model xml file.
    """
    if model_name is None:
        model_name = "myoskeleton.xml"
    model_path = os.path.join(curr_dir, "../myoskeleton", model_name)
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found: {model_path}")
    return model_path


def get_assets_path():
    """Get the path to the assets directory.

    Returns:
        str: Path to the assets directory.
    """
    return os.path.join(curr_dir, "../myoskeleton")


def get_markerset_path(markerset_name="metrabs"):
    """Get the path to the markerset file.

    Args:
        markerset_name (str): Name of the markerset to retrieve.
                              Available: cmu, metrabs

    Returns:
        str: Path to the markerset file.
    """
    markerset_dict = {
        "cmu": "cmu_markerset.xml",
        "metrabs": "movi_metrabs_markerset.xml",
    }

    if markerset_name not in markerset_dict:
        raise ValueError(
            f"Invalid markerset: {markerset_name}. Available: {list(markerset_dict.keys())}"
        )

    markerset_path = os.path.join(
        curr_dir, "../markerset", markerset_dict[markerset_name]
    )
    if not os.path.exists(markerset_path):
        raise FileNotFoundError(f"Markerset file not found: {markerset_path}")

    return markerset_path
