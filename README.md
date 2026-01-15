
# MyoModel

**MyoModel** is a library of carefully constructed Musculoskeletal Models.

## Overview
Musculoskeletal models are one the fundamental building blocks in diverse fields - biomechanics, graphics, animation, rehabilitation, etc. Given their significance, there is a rich history of musculoskeletal modeling efforts by multiple groups over decades. In addition to varying convensions, such efforts face two key challenges -
  1. sparsity of experimental data - leading to localized incomplete models
  2. computational challenges - in capturing the full human anatomy

The goal of MyoModel is to develop a compherensive library that unifies the fragmented developments from disjoint fields, while meeting the computational challenges involved in capturing full details of human anatomy.

## Usage
There are multiple ways to explore and leverage MyoModel
  - MyoModel: For any needs involving *only* access to the models, [myo_model](https://github.com/myolab/myo_model) (this repo) is all you need
  - MyoAPI: For programmatic access to the models and basic developmental needs, please refer to [myo_api](https://github.com/myolab/myo_api) repo

## Example usage
NOTE: To use the models ```pip install myo_model``` using MyoPyPi

1. myoskeleton without any actuators or skins
```
from myo_model.utils import model_utils
from myo_api.mjs.core import mjs_api

model_path = model_utils.get_model_xml_path()
assets_path = model_utils.get_assets_path()

model_spec, _ = mjs_api.get_model_spec(model_path, assets_path)
mj_model = model_spec.compile()
```

2. myoskeleton with skinned muscles and the mecka markerset
```
from myo_model.utils import model_utils
from myo_api.mjs.marker import marker_api

model_path = model_utils.get_model_xml_path("body_skin")
assets_path = model_utils.get_assets_path()
markerset_path = model_utils.get_markerset_path("mecka")


model_spec, _, _ = marker_api.apply_marker_set(model_path, assets_path, markerset_path)
mj_model = model_spec.compile()
```
## Local testing of asset downloads

The CI is not configured to test asset downloads till the code is merged into main. For local testing run the code in the example folder

```
conda create -n "model_env"
conda activate model_env
pip install myo_model
python "path/to/install"/myo_model/example/load_model.py
```

## Citation
```bibtex
@techreport{myoskeleton,
  author      = {Vittorio Caggiano AND Vittorio La Barbera AND Andrea Prestia AND Ouassim Aouattah AND Pierre Schumacher AND Varun Joshi AND Vikash Kumar},
  title       = {MyoSkeleton: A Universal Human Skeletal Model},
  institution = {MyoLab Inc.},
  year        = {2024},
  type        = {White Paper},
  note        = {Available at: \url{https://github.com/myolab/myo_model}},
}
```
