import PyInstaller.__main__
import os

# Параметры для сборки
PyInstaller.__main__.run([
    'script.py',
    '--onefile',
    '--windowed',
    '--name=Radioactive Decay Simulator',
    '--add-data=requirements.txt;.',
    '--hidden-import=numpy._core._exceptions',
    '--hidden-import=numpy._core._multiarray_umath',
    '--hidden-import=matplotlib',
    '--hidden-import=matplotlib.backends.backend_agg',
    '--hidden-import=matplotlib.backends.backend_tkagg',
])