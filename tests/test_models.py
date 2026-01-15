"""
Copyright (c) 2026 MyoLab, Inc.
Released under the MyoLab Non-Commercial Scientific Research License
on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
either express or implied.

You may not use this file except in compliance with the License.
See the LICENSE file for governing permissions and limitations.
"""

# Summary: Test suite for model loading and validation

import glob
import os

import mujoco
import pytest

from myo_model.utils.model_utils import get_model_xml_path

curr_dir = os.path.dirname(os.path.realpath(__file__))

MYOSKELETON_DIR = os.path.dirname(get_model_xml_path())

# Get all XML files in the myoskeleton folder
MYOSKELETON_MODELS = glob.glob(os.path.join(MYOSKELETON_DIR, "*.xml"))


@pytest.mark.parametrize(
    "model_handle",
    MYOSKELETON_MODELS,
)
def test_model(model_handle):
    print(f"Testing: {model_handle}")

    # Load from xml path
    mj_model = mujoco.MjModel.from_xml_path(str(model_handle))
    mj_data = mujoco.MjData(mj_model)

    # Simulate for 2 timesteps
    for i in range(2):
        mujoco.mj_step(mj_model, mj_data)


if __name__ == "__main__":
    # Test all models
    for model in MYOSKELETON_MODELS:
        test_model(model)
