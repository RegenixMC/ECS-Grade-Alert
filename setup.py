from cx_Freeze import setup, Executable

if int(input('Type 1 to compile init, type 2 to compile database_manager: ')) == 1:
      setup(name = "ECS Alert System" ,
            version = "0.1" ,
            description = "" ,
            executables = [Executable("__init__.py")])

else:
      setup(name = "ECS Alert System" ,
            version = "0.1" ,
            description = "" ,
            executables = [Executable("databaseManager.py")])