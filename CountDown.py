#Original: https://flet.dev/docs/guides/python/user-controls/

import flet as ft
import time, threading

class Countdown(ft.UserControl):
    def __init__(self, seconds):
        super().__init__()
        self.seconds = seconds
        self.flg = True
        self.timeValue = 1200
        self.progress = ft.ProgressBar
        self.progress.value = self.timeValue

    def did_mount(self):
        self.running = True
        self.th = threading.Thread(target=self.update_timer, args=(), daemon=True)
        self.th.start()

    def will_unmount(self):
        self.running = False    

    def dialog_open(self):
        def restart(e):
            self.page.window_always_on_top = False
            self.page.update()
            self.timeValue = 1200
            self.flg = True
            self.seconds = self.timeValue
            self.did_mount()

        self.page.window_always_on_top = True
        dlg = ft.AlertDialog(title=ft.Text("Take a rest."),on_dismiss=restart)
        self.page.dialog = dlg
        dlg.open = True        
        self.page.update()

    def update_timer(self):
        while self.seconds and self.running:
            mins, secs = divmod(self.seconds, 60)
            self.countdown.value = "{:02d}:{:02d}".format(mins, secs)
            self.update()
            time.sleep(1)
            if self.flg == True:
                self.seconds -= 1
        self.countdown.value="00:00"
        self.update()
        self.dialog_open()

    def build(self):
        def reset(e):
            self.timeValue = 1201
            self.flg = True
            if self.seconds == 0:
                self.seconds = self.timeValue
                self.th = threading.Thread(target=self.update_timer, args=(), daemon=True)
                self.th.start()
            else:
                self.seconds = self.timeValue

        def switch(e):
            if self.flg == True:
                self.flg = False
            else:
                self.flg = True        

        self.countdown = ft.Text(size=100)
        self.reset = ft.ElevatedButton("Reset",on_click=reset)
        self.pause = ft.ElevatedButton("Pause",on_click=switch)
        return ft.Column([
            ft.Row([
                self.countdown
            ],alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([
                self.reset,
                self.pause
            ],alignment=ft.MainAxisAlignment.CENTER)
        ]),

def main(page: ft.Page):
    page.title="タイマーだよ～ん"
    page.window_center()
    page.window_resizable=False
    page.window_width=400
    page.window_height=300
    page.bgcolor=ft.colors.BLUE_GREY_200
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.add(Countdown(1200))

ft.app(target=main)