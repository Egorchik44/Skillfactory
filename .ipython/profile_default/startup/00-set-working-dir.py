"""
Автоматическая настройка рабочей директории для всех Jupyter ноутбуков
Этот файл выполняется автоматически при запуске ядра IPython/Jupyter
"""
import os

PROJECT_ROOT = r'C:\Users\PC\Downloads\Project_SF'

if os.getcwd() != PROJECT_ROOT:
    try:
        os.chdir(PROJECT_ROOT)
        print(f"✓ Рабочая директория автоматически установлена: {PROJECT_ROOT}")
    except Exception as e:
        print(f"⚠ Не удалось установить рабочую директорию: {e}")
