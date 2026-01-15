"""
Copyright (c) 2026 MyoLab, Inc.
Released under the MyoLab Non-Commercial Scientific Research License
on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
either express or implied.

You may not use this file except in compliance with the License.
See the LICENSE file for governing permissions and limitations.
"""

# Summary: Example script: load_model_with_markers

import os

from myo_tools.mjs.core import mjs_api
from myo_tools.mjs.marker import marker_api

from myo_model.utils import model_utils

model_path = model_utils.get_model_xml_path()
assets_path = os.path.dirname(model_utils.get_assets_path())

model_spec, _ = mjs_api.get_model_spec(model_path)
mj_model = model_spec.compile()

model_path = model_utils.get_model_xml_path()
markerset_path = model_utils.get_markerset_path("metrabs")

model_spec, _, _ = marker_api.apply_marker_set(model_path, assets_path, markerset_path)
mj_model = model_spec.compile()

print("Succesfullly loaded myoskeleton with metrabs markerset")
