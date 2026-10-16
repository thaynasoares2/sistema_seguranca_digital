"""Instalação local portátil, com bibliotecas incluídas e senha escolhida no destino."""
from pathlib import Path
import argparse, getpass, os, subprocess, sys, venv
ROOT = Path(__file__).resolve().parent
APP = ROOT / 'sistema'
def python_venv():
    return ROOT / '.venv' / ('Scripts/python.exe' if os.name == 'nt' else 'bin/python')
def run(args, env=None):
    subprocess.run([str(python_venv()), *args], cwd=APP, env=env, check=True)
def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--verificar', action='store_true', help='Executar também os testes do sistema.')
    args = parser.parse_args()
    if sys.version_info < (3, 10):
        raise SystemExit('Use Python 3.10 ou superior; este pacote foi testado com Python 3.13.')
    try:
        import sqlite3
    except ImportError:
        raise SystemExit('Este Python precisa incluir SQLite. Instale uma distribuição completa de Python.')
    print('Criando o ambiente local...')
    if not python_venv().exists():
        venv.EnvBuilder(with_pip=True).create(ROOT / '.venv')
    run(['-m', 'pip', 'install', '--no-index', '--find-links', str(ROOT / 'dependencias'), '-r', str(ROOT / 'requirements_offline.txt')])
    run(['manage.py', 'migrate', '--noinput'])
    run(['manage.py', 'importar_matriz', 'docs/MATRIZ_CONTROLES_v0.csv', '--versao', 'v0.1'])
    marker = ROOT / '.instalacao-concluida'
    if not marker.exists():
        while True:
            password = getpass.getpass('Escolha uma senha para os quatro usuários Alpha (mínimo 12 caracteres): ')
            if len(password) < 12:
                print('Use ao menos 12 caracteres.'); continue
            if password != getpass.getpass('Repita a senha: '):
                print('As senhas não coincidem.'); continue
            break
        env = os.environ.copy()
        env['TCC_DEMO_PASSWORD'] = password
        run(['manage.py', 'seed_alpha', '--versao', 'v0.1'], env=env)
        env.pop('TCC_DEMO_PASSWORD', None)
        del password
        marker.write_text('Beta S2 instalada; senhas escolhidas localmente.\n')
    else:
        print('Instalação já existente; usuários e senhas anteriores preservados.')
    run(['manage.py', 'check'])
    if args.verificar:
        run(['manage.py', 'test', 'avaliacao'])
    print('Instalação concluída. Execute iniciar.bat (Windows) ou sh iniciar.sh (Linux/macOS).')
    print('Abra http://127.0.0.1:8000/ e use alpha_gestor com a senha escolhida nesta instalação.')
if __name__ == '__main__':
    try:
        main()
    except subprocess.CalledProcessError as error:
        raise SystemExit(f'Instalação interrompida: etapa retornou {error.returncode}. Confira a mensagem acima.')
