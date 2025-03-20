from cx_Freeze import setup, Executable
import os
path = "./assets/"
assets_list = os.listdir(path)
assets_list_completa = [os.path.join(path, assets).replace(__old="//", __new="/") for assets in assets_list]
print(assets_list_completa)

executables = [Executable("main.py")]
files = {"include_files": assets_list_completa, "packages": ["pygame"]}

setup(
    name="Mountain Project",
    version="1.0",
    description="Mountain Shooter app",
    options={"build_exe": {"packages": ["pygame"]}},
    executables=executables,
)