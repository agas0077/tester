[flake8]
accept-encodings = utf-8
statistics = False
max-line-length = 79
doctests = False
enable-extensions = G
isort-show-traceback = True

exclude =
  .git,
  .venv,
  .vscode/*.py,
  pycache,
  /site-packages//*.py,
  migrations

extend-ignore = E203

ignore =
    C901,
    F40,
    E211,
    E225,
    E226,
    E231,
    E303,
    E711,
    E712,

[isort]
profile = black
import_heading_stdlib=Standard Library
import_heading_thirdparty=Third Party Library
import_heading_localfolder=Local Modules
known_local_folder = src
line_length = 79
multi_line_output = 3
include_trailing_comma = True
force_grid_wrap = 0
use_parentheses = True
ensure_newline_before_comments = True