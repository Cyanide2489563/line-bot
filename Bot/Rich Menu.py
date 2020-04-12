# coding: utf-8
from linebot.models import RichMenu, RichMenuSize, RichMenuArea, RichMenuBounds, URIAction

from Bot.Main import line_bot_api

rich_menu_to_create = RichMenu(
    size=RichMenuSize(width=2500, height=843),
    selected=False,
    name="測試用 Rich Menu",
    chat_bar_text="點擊開啟 Rich Menu",
    areas=[
        RichMenuArea(
            bounds=RichMenuBounds(x=0, y=0, width=2500, height=843),
            action=URIAction(label='Go to line.me', uri='https://line.me')),
        RichMenuArea(
            bounds=RichMenuBounds(x=0, y=0, width=2500, height=843),
            action=URIAction(label='Go to line.me', uri='https://line.me'))
    ]
)
rich_menu_id = line_bot_api.create_rich_menu(rich_menu=rich_menu_to_create)
var = line_bot_api.setDefaultRichMenu(rich_menu_id)
