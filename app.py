import sys, os
print("Python exe:", sys.executable)
print("VIRTUAL_ENV:", os.environ.get("VIRTUAL_ENV"))
print(sys.executable.endswith(r".venv\\Scripts\\python.exe"))
