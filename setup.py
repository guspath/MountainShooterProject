from cx_Freeze import setup, Executable

executables = [Executable("main.py")]

setup(
    name="Mountain Project",
    version="1.0",
    description="Mountain Shooter app",
    options={"build_exe": {"packages": ["pygame"]}},
    executables=executables,
)
