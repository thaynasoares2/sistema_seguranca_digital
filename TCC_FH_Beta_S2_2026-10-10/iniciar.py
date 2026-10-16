from pathlib import Path
import os, subprocess
root = Path(__file__).resolve().parent
python = root / '.venv' / ('Scripts/python.exe' if os.name == 'nt' else 'bin/python')
if not python.exists() or not (root / '.instalacao-concluida').exists():
    raise SystemExit('Execute o instalador antes de iniciar o sistema.')
print('Acesse http://127.0.0.1:8000/ . Para encerrar, use Ctrl+C.', flush=True)
raise SystemExit(subprocess.call([str(python), 'manage.py', 'runserver', '127.0.0.1:8000', '--noreload'], cwd=root / 'sistema'))
