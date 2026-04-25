@echo off
setlocal

cd /d "%~dp0"

echo Setting up backend...
if not exist ".venv\Scripts\python.exe" (
    python -m venv .venv
)

call .venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r backend\requirements.txt
pip install -e library_sdk
python -m alembic -c backend\alembic.ini upgrade head
python -c "import pathlib, sqlite3; db=pathlib.Path('backend/library.db'); sql=pathlib.Path('backend/seed_data.sql').read_text(); con=sqlite3.connect(db); con.executescript(sql); con.commit(); con.close()"

echo Setting up frontend...
cd frontend
npm install
cd ..

echo Setup complete.
