# импортируем библиотеки
import asyncio
import flet as ft

# создаем главную функцию
async def main(page: ft.Page) -> None:
    # page.window.always_on_top = True # окно с приложением всегда наверху
    # настраеваем вид страницы
    page.title = "HSEcoin"
    page.theme_mode = ft.ThemeMode.DARK
    # page.bgcolor = "#141221"
    page.bgcolor = ft.colors.TRANSPARENT # прозрачный цвет страницы
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    # настройка фона
    page.decoration = ft.BoxDecoration(
        # задание изображения
        image = ft.DecorationImage(
            src = 'bg2.jpg',
            fit=ft.ImageFit.COVER,
            # opacity=0.6
        ),
        # создание градиента
        # gradient = ft.LinearGradient(
        #     colors=[ft.colors.BLUE, ft.colors.TRANSPARENT],
        #     stops=[0, 0.5],
        #     begin=ft.alignment.bottom_center,
        #     end=ft.alignment.top_center
        # ),
    )
    # делаем красивый шрифт
    page.fonts = {"FulboArgenta":  "fonts/ofont.ru_Fulbo Argenta.ttf"}
    page.theme = ft.Theme(font_family="FulboArgenta") 
    # бар с кнопками внизу страницы
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.EXPLORE, label="Explore"),
            ft.NavigationBarDestination(icon=ft.icons.COMMUTE, label="Commute"),
            ft.NavigationBarDestination(icon=ft.icons.BOOKMARK_BORDER, selected_icon=ft.icons.BOOKMARK, label="Explore"),
            ft.NavigationBarDestination(icon=ft.icons.MONEY, label="Balance"),
        ]
    )

    # анимация тапа по монетке
    async def score_up(event: ft.ContainerTapEvent):
        score.data += 1
        score.value = str(score.data)

        image.scale = 0.95

        score_counter.opacity = 1
        score_counter.value = "+1"
        score_counter.right = 0
        score_counter.left = tap_position[0]
        score_counter.top = tap_position[1]
        score_counter.bottom = 0

        # заполнение прогресс бара
        # progress_bar.value += (1 / 50)

        # if score.data % 50 == 0:
        #     page.snack_bar = ft.SnackBar(
        #         content=ft.Text(
        #             value="+50 points",
        #             size=20,
        #             color="#00a9ff",
        #             text_align=ft.TextAlign.CENTER
        #         ),
        #         bgcolor="#003399"
        #     )
        #     page.snack_bar.open = True
        #     progress_bar.value = 0

        await page.update_async()

        await asyncio.sleep(0.1)
        image.scale = 1
        score_counter.opacity = 0

        await page.update_async()


    def on_tap_down(event: ft.ContainerTapEvent):
        global tap_position
        tap_position = (event.local_x, event.local_y)

    score = ft.Text(value="0", size=100, data=0)
    score_counter = ft.Text(
        size=50, animate_opacity=ft.Animation(duration=600, curve=ft.AnimationCurve.BOUNCE_IN)
    )

    image = ft.Image(
        src="coin.png",
        fit=ft.ImageFit.CONTAIN,
        animate_scale=ft.Animation(duration=600, curve=ft.AnimationCurve.EASE)
    )
    # progress_bar = ft.ProgressBar(
    #     value=0,
    #     width=page.width - 100,
    #     bar_height=20,
    #     color="#00a9ff",
    #     bgcolor="#003399"
    # )


    await page.add_async(
        score,
        ft.Container(
            content = ft.Stack(controls = [image, score_counter]),
            on_click = score_up,
            on_tap_down = on_tap_down,
            margin = ft.Margin(0, 0, 0, 30)
        ),
        # ft.Container(
        #     content=progress_bar,
        #     border_radius=ft.BorderRadius(10, 10, 10, 10)
        # )
    )

# запуск программы
if __name__ == "__main__":
    tap_position = (0, 0)
    #ft.app(target=main, view=None, port=8000)
    ft.app(main) # для провеки того, что получилось