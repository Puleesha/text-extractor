1. Create the virtual environment with Python 3.10

```bash
brew install python@3.10
/opt/homebrew/bin/python3.10 -m venv .venv
source .venv/bin/activate
```
for macos, or 
```bash
pip install python@3.10
python -m venv .venv
.venv\Scripts\activate
```for windows.

2. Clone the repo in the .venv and install packages

```bash
git clone https://github.com/microsoft/markitdown.git 
cd markitdown
pip install -e 'packages/markitdown[all]'
```


## For marker:

1. Activate the virtual environment

```bash
source .venv/bin/activate
```
for macos, or 
```bash
.venv\Scripts\activate
```
for windows.

2. Then install the dependency and start the analysis (very RAM heavy!!!)

```bash
pip install marker-pdf
marker_single odel_report.pdf
```

## For camelot: 

1. Create the virtual environment with Python 3.10

```bash
brew install python@3.10
/opt/homebrew/bin/python3.10 -m venv .venv
source .venv/bin/activate
```

2. Install camelot

```bash
pip install camelot-py
pip install tabulate
```



