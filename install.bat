echo "Prepare virtual environment"

python -m virtualenv .venv
.\.venv\Scripts\pip.exe install -r .\requirements.txt
.\.venv\Scripts\pip.exe install -e .

echo "Finish"
