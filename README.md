# CSE4283-Test-Project
A project designed for practicing Test Driven Development for CSE4283 - Software Testing and Quality Assurance.

# Windows
1) Navigate to directory with downloaded files
2) In command prompt, run ```python3 -m venv .```
3) Then, run ```.\Scripts\pip3.exe install pytest```
4) Then, run ```.\Scripts\pytest.exe --ignore=Lib``` to test the code
5) Finally, run ```.\Scripts\python.exe main.py``` to run the code

# Linux
## Environment Setup
1) Create Virtual Environment
```bash
python3 -m venv .
```

2) Activate Virtual Environment

```bash
source bin/activate
```

3) Install pytest
```bash
pip install -U pytest
```

## Run Application
While in virtual environment (see Setup step 2),
```bash
python3 main.py
```

## Test Application
While in virtual environment (see Setup step 2),
```bash
pytest
```
