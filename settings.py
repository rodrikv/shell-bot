import os

TOKEN = os.environ.get("TELEGRAM_API_TOKEN", '')

PORT = int(os.environ.get("PORT", "8443"))
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", "telegram-shell-bot")
IS_HEROKU = os.environ.get("IS_HEROKU", False)

# Set users to -999999 to disable user authentication
ENABLED_USERS = os.environ.get("ENABLED_USERS", '')
ENABLED_USERS = set(int(e.strip()) for e in ENABLED_USERS.split(','))  # type: ignore

CMD_WHITE_LIST = set()
CMD_BLACK_LIST = {'rm'}
CMD_BLACK_CHARS = {';', '\n', "&"}
ONLY_SHORTCUT_CMD = False

MAX_TASK_OUTPUT = int(os.environ.get("MAX_TASK_OUTPUT", 99999))

PROXY_URL = os.environ.get("ALL_PROXY", '')

SC_MENU_ITEM_ROWS = (
    (
        ('pwd', 'pwd'),  # display name, command, is script
        ('ls', 'ls'),
        ('ls -lh', 'ls -lh'),
    ),
    (
        ('ls -lha', 'ls -lha'),
    ),
)

SC_MENU_ITEM_CMDS = {}
for row in SC_MENU_ITEM_ROWS:
    for cmd in row:
        SC_MENU_ITEM_CMDS[cmd[1]] = cmd

REQUEST_KWARGS = {
    'proxy_url': PROXY_URL
}

ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
SCRIPTS_ROOT_PATH = os.path.join(ROOT_PATH, 'scripts')
UPLOAD_PATH = os.path.join(ROOT_PATH, 'upload')
