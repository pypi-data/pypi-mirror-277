import os
import time

import mujoco
import mujoco.viewer

if __name__=="__main__":
    model_filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rearrangement.mjb')
    m = mujoco.MjModel.from_binary_path(model_filepath)
    d = mujoco.MjData(m)

    # Iterate through cameras and print their names and IDs
    for camera_id in range(m.ncam):
        camera_name = mujoco.mj_id2name(m, mujoco.mjtObj.mjOBJ_CAMERA, camera_id)

    with mujoco.viewer.launch_passive(
        model=m, 
        data=d,
        show_left_ui=False,
        show_right_ui=False,
        ) as viewer:
            while viewer.is_running():
                time.sleep(0.05)
                viewer.sync()


