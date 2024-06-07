from textual.app import App, ComposeResult
from textual.widgets import Static, Label

# https://passwordpassword.online
HEADER = """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣦⣤⣴⣦⣤⣤⠀⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣤⣴⣶⡟⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠉⢉⠟⠀⠀⠀⠀⠉⠛⣿⠛⠷⡄⣀⠀⠀⠀⠀
⠀⠀⢀⣤⠞⣻⠉⠉⠀⠀⠀⠈⢣⡀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠐⠀⠀⠀⠀⣧⠀⡄⢉⡿⠀⠀⠀
⠀⣴⠋⠀⠀⡇⠀⠀⠀⠐⠀⠀⢸⡇⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠀⠀⠤⣀⠀⠀⠀⢀⡟⠀⠀⠋⠀⠀⠀⠀
⠈⠈⠃⠀⠀⠧⠀⣀⠀⠠⠔⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠉⠉
client: {}; api: {}; mpv: {}⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

# add widget for ongoing
# https://github.com/Textualize/toolong/blob/main/src/toolong/log_lines.py#L130

class Anicli(App):
    def compose(self) -> ComposeResult:
        yield Label(HEADER.format(1, 2 , 3))


if __name__ == '__main__':
    Anicli().run()