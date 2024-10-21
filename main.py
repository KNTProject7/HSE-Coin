from flet import *

def main(page: Page):
    page.bgcolor = "black"

    page.add(
        Column([
        Text("Success deploy to cloudflare", size=30, weight="bold")
        ])
    )

flet.app(target=main)