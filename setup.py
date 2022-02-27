from cx_Freeze import setup, Executable

setup(name="EDUway",
      version='0.1',
      description='Education',
      executables=[Executable("main.py")])
