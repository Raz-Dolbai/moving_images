import sys
from cx_Freeze import setup, Executable

executables = [Executable('open.py',
                          targetName='CopyImage.exe',
                          base='Win32GUI',
                          icon='chocolate_chip_chips_food_cookies_biscuit_icon_207973.ico')]

zip_include_packages = ['collections', 'encodings', 'importlib', '_distutils_hack', 'asyncio', 'ctypes', 'concurrent',
                        'curses', 'email', 'html', 'lib2to3', 'logging',
                        'msilib', 'multiprocessing', 'pkg_resources', 'pydoc_data', 'setuptools', 'sqlite3', 'test',
                        'unittest','dateutil','distutils','et_xmlfile', 'http', 'json', 'numpy', 'openpyxl',
                        'pandas', 'pytz', 'tkinter', 'urllib', 'xlsxwriter', 'xml', 'xmlrpc' ]

# excludes = ['_distutils_hack', 'asyncio', 'ctypes', 'concurrent', 'curses', 'email', 'html', 'lib2to3', 'logging',
# 'msilib', 'multiprocessing', 'pkg_resources', 'pydoc_data', 'setuptools', 'sqlite3', 'test',
# 'unittest', ]

# добавляем в options 'excludes': excludes

options = {
    'build_exe': {'build_exe': 'build_windows',
                  'include_msvcr': True,
                  'zip_include_packages': zip_include_packages}
}

setup(
    name="Image",
    version="0.1",
    description="CopyImage",
    options=options,
    executables=executables
)
