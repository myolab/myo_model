# MyoModel

**MyoModel** is a library of carefully constructed Musculoskeletal Models.
![banner](https://github.com/user-attachments/assets/87897766-cf55-4932-936f-dc53711976ef)


## Overview
Musculoskeletal models are one the fundamental building blocks in diverse fields - biomechanics, graphics, animation, rehabilitation, etc. Given their significance, there is a rich history of musculoskeletal modeling efforts by multiple groups over decades. In addition to varying conventions, such efforts face two key challenges -
  1. sparsity of experimental data - leading to localized incomplete models
  2. computational challenges - in capturing the full human anatomy

The goal of MyoModel is to develop a comprehensive library that unifies the fragmented developments from disjoint fields while meeting the computational challenges involved in capturing full details of human anatomy.

## Usage
There are multiple ways to explore and leverage MyoModel
  - MyoModel: For any needs involving *only* access to the models, [myo_model](https://github.com/myolab/myo_model) (this repo) is all you need
  - MyoTools: For programmatic access to the models and basic developmental needs, please refer to [myo_tools](https://github.com/myolab/myo_tools) repo
  - MyoSuite: For building data-driven behavioral controllers for the models, please refer to [myosuite](https://github.com/MyoHub/myosuite) repo

## License
A permissive license for non-commercial scientific research is available [here](LICENSE).

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

## Example usage
```python
import mujoco
import mujoco.viewer
from myo_model.utils import model_utils

model_path = model_utils.get_model_xml_path()
mj_model = mujoco.MjModel.from_xml_path(model_path)

# Make the data object
mj_data = mujoco.MjData(mj_model)

# Run the viewer
with mujoco.viewer.launch_passive(
    mj_model, mj_data) as viewer:
    while viewer.is_running():
        viewer.sync()
```
