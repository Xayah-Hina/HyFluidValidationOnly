import hou
import os


### Please use Hython instead of common Python
### You can find Hython under Houdini Installed dir
### Eg. "C:/Program Files/Side Effects Software/Houdini 20.5.550/bin/hython.exe"

def export_density_field(den, save_path, surname, bbox):
    resx, resy, resz = den.shape[0], den.shape[1], den.shape[2]
    geo = hou.Geometry()
    vol = geo.createVolume(resx, resy, resz, hou.BoundingBox(*bbox))
    vol.setAllVoxels(den.cpu().numpy().flatten().tolist())
    os.makedirs(save_path, exist_ok=True)
    output_path = os.path.join(save_path, f"{surname}.bgeo.sc")
    geo.saveToFile(output_path)
    print(f"Save {output_path}")


def export_velocity_field(vel, save_path, surname, bbox):
    resx, resy, resz = vel.shape[0], vel.shape[1], vel.shape[2]
    geo = hou.Geometry()
    vel_np = vel.cpu().numpy()
    name_attrib = geo.addAttrib(hou.attribType.Prim, "name", "default")
    for i, name in enumerate(['vel.x', 'vel.y', 'vel.z']):
        vol = geo.createVolume(resx, resy, resz, hou.BoundingBox(*bbox))
        vol.setAttribValue(name_attrib, name)
        data_flat = vel_np[..., i].flatten().tolist()
        vol.setAllVoxels(data_flat)
    os.makedirs(save_path, exist_ok=True)
    output_path = os.path.join(save_path, f"{surname}.bgeo.sc")
    geo.saveToFile(output_path)
    print(f"Save {output_path}")
