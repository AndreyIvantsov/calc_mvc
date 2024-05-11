import tkinter as tk
from tkinter import ttk


class View(tk.Tk):

    PAD = 10
    MAX_BUTTONS_PER_ROW = 4
    BUTTON_CAPTIONS = [
        'C', '+/-', '%', '/',
        7, 8, 9, '*',
        4, 5, 6, '-',
        1, 2, 3, '+',
        0, '.', '=',
    ]

    def __init__(self, controller) -> None:
        super().__init__()
        self.title('PyCalc 1.0')
        self.config(bg='darkgray')
        self.ctrl = controller
        self.value_var = tk.StringVar()
        self._configure_button_style()
        self._make_main_frame()
        self._make_label()
        self._make_buttons()
        self._center_window()

    def main(self):
        self.mainloop()

    def _configure_button_style(self):
        # 'winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative'
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('N.TButton',  foreground='white', background='gray')
        style.configure('O.TButton',  foreground='white', background='orange')
        style.configure('M.TButton',  foreground='gray')
        print(style.theme_names())
        print(style.theme_use())

    def _make_main_frame(self):
        self.main_frm = ttk.Frame(self)
        self.main_frm.pack(padx=self.PAD, pady=self.PAD)

    def _make_label(self):
        lbl = tk.Label(
            self.main_frm,
            textvariable=self.value_var,
            anchor=tk.E,
            background='black',
            foreground='white',
            font=('Arial', 30)
        )
        lbl.pack(fill=tk.X)

    def _make_buttons(self):
        outer_frm = ttk.Frame(self.main_frm)
        outer_frm.pack()

        is_first_row = True
        buttons_in_row = 0

        for caption in self.BUTTON_CAPTIONS:
            if is_first_row or buttons_in_row == self.MAX_BUTTONS_PER_ROW:
                is_first_row = False
                inner_frm = ttk.Frame(outer_frm)
                inner_frm.pack(fill=tk.X)
                buttons_in_row = 0

            if isinstance(caption, int):
                style_prefix = 'N'
            elif caption in ['/', '*', '-', '+', '=']:
                style_prefix = 'O'
            else:
                style_prefix = 'M'

            style_name = f'{style_prefix}.TButton'

            btn = ttk.Button(
                inner_frm,
                text=caption,
                command=(lambda btn=caption: self.ctrl.on_button_click(btn)),
                # width=10,
                style=style_name,
            )

            if caption == '=':
                fill = tk.X
                expand = 1
            else:
                fill = tk.NONE
                expand = 0

            btn.pack(fill=fill, expand=expand, side=tk.LEFT)
            buttons_in_row += 1

    def _center_window(self):
        self.update()
        width = self.winfo_width()
        height = self.winfo_height()
        x_offset = (self.winfo_screenwidth() - width) // 2
        y_offset = (self.winfo_screenheight() - height) // 2
        self.geometry(f'{width}x{height}+{x_offset}+{y_offset}')
