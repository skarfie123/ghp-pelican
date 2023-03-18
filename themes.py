import os
import subprocess
import tkinter as tk
import webbrowser
from pathlib import Path


def main():
    root = tk.Tk()
    root.title("Tkinter Example")

    label = tk.Label(root, text="Hello, Tkinter!")
    width = 10
    label.grid(row=0, column=0, columnspan=width + 1)

    def on_button_click(f):
        label.config(text=f"{f.name} clicked!")
        args = [
            "pelican",
            "content",
            "-o",
            "output",
            "-e",
            f'SITENAME="{f.name}"',
            "-t",
            str(f),
        ]
        print(args, " ".join(args))
        subprocess.run(
            args,
            check=True,
        )

    themes_path = Path(os.getenv("GITHUB")) / "pelican-themes"

    i = 1
    for file in themes_path.iterdir():
        if not file.is_dir() or file.name.startswith("."):
            continue
        button = tk.Button(
            root, text=file.name, command=lambda f=file: on_button_click(f)
        )
        button.grid(row=(i - 1) // width + 1, column=(i - 1) % width)
        i += 1

    button = tk.Button(
        root, text="open", command=lambda: webbrowser.open("http://127.0.0.1:8000/")
    )
    button.grid(row=(i - 1) // width + 2, column=0, columnspan=width + 1)

    root.mainloop()


if __name__ == "__main__":
    main()
