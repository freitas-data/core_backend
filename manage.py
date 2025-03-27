#!/usr/bin/env python
import os
import sys
from decouple import config  # adicionado para usar .env

def main():
    """Ponto de entrada para comandos de gerenciamento Django."""
    os.environ.setdefault(
        'DJANGO_SETTINGS_MODULE',
        config('DJANGO_SETTINGS_MODULE', default='config.settings.dev')
    )
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Não foi possível importar Django. Está instalado no seu ambiente?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
