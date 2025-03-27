#!/usr/bin/env python
import os
import sys
from pathlib import Path
from decouple import config, AutoConfig

def main():
    """Ponto de entrada para comandos de gerenciamento Django."""
    # Configura caminho do .env (raiz do projeto)
    BASE_DIR = Path(__file__).resolve().parent
    config = AutoConfig(search_path=BASE_DIR)

    try:
        # Carrega o módulo de settings
        settings_module = config(
            'DJANGO_SETTINGS_MODULE',
            default='core_backend.settings'  # Ajuste para seu caminho real
        )
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Is it installed and available?"
        ) from exc
    except Exception as e:
        raise RuntimeError(f"Erro na configuração: {e}") from e

    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()