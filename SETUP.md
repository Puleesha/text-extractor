1. Create the virtual environment with Python 3.10

```bash
brew install python@3.10
/opt/homebrew/bin/python3.10 -m venv .venv
source .venv/bin/activate
```

2. Clone the repo in the .venv and install packages

```bash
git clone https://github.com/microsoft/markitdown.git 
cd markitdown
pip install -e 'packages/markitdown[all]'
```



