import flet as ft
import functions
from functions import api_key
from collections import defaultdict
from datetime import datetime

def main(page: ft.Page):

    #Funções: 
    def update_climate(e):
        city, country = pesquisa_local.value.strip().split(",")

        climate = functions.get_climate_by_name(api_key, city=city, country=country)
        days_climate = functions.days_predict(api_key, city=city, country=country)

        user_city_name = climate['name']
        user_climate_icon = climate['weather'][0]["icon"]
        user_climate_temperature = climate['main']["temp"]
        user_climate_humidity = climate['main']["humidity"]

        cnt_central_linha1.controls[0].value = user_city_name
        cnt_central_linha2.controls[0].src = f"https://openweathermap.org/img/wn/{user_climate_icon}@2x.png"
        cnt_central_linha3.controls[0].value = f"C° {int(user_climate_temperature)}"
        cnt_central_linha4.controls[0].value = f"Umidade: % {user_climate_humidity}"

        # Previsão dos próximos dias
        max_temp_day = defaultdict(lambda: ("", "", float("-inf")))

        for predict in days_climate["list"]:
            data = datetime.fromtimestamp(predict['dt'])
            days = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sab", "Dom"]
            day_week = days[data.weekday()]
            chave = data.strftime('%Y/%m/%d')

            icon_tmp = predict["weather"][0]["icon"]
            temp_tmp = int(predict["main"]["temp"])

            if icon_tmp.endswith('d'):  # Apenas previsão do dia
                if temp_tmp > max_temp_day[chave][2]:
                    max_temp_day[chave] = (day_week, icon_tmp, temp_tmp)

        
        for i, (data, (dia, icon, temp)) in enumerate(sorted(max_temp_day.items())[:5]):
            cnt_inferior_linha1.controls[i].value = dia
            cnt_inferior_linha2.controls[i].src = f"https://openweathermap.org/img/wn/{icon}@2x.png"
            cnt_inferior_linha3.controls[i].value = f"{temp}°C"

        page.update()

    def get_user_location(e):
        lista_inf_ip = functions.get_user_cords()

        lat = lista_inf_ip[0]
        long = lista_inf_ip[1]
        city = lista_inf_ip[2]
        region = lista_inf_ip[3]
        country= lista_inf_ip[4]

        pesquisa_local.value = f"{city}, {country}"
        pesquisa_local.update()

        update_climate(e)

    page.bgcolor = ft.colors.BLACK
    page.title = "Clima Tempo"
    page.window.width = 400
    page.window.height = 844
    

    
    # container principal, onde os outros containers serão adicionados
    cnt_principal = ft.Container(

        bgcolor=ft.colors.BLUE,
        border_radius=35,
        padding = 10,
        width= page.window.width * 0.90,
        height= page.window.height * 0.92,
        content=ft.Column(
            alignment= ft.MainAxisAlignment.SPACE_BETWEEN,
            height=page.window.height * 0.90,
            width=page.window.width * 0.90,


        )
    )
    #---------------------------------------------------------------------------------
    # Container superior:

    cnt_superior = ft.Container(
        #bgcolor= ft.colors.WHITE,
        height = 100,
        width = cnt_principal.width * 0.95,
        content= ft.Row(

        )
    )

    pesquisa_local = ft.TextField(
        bgcolor=ft.colors.GREY_100,
        border_color=ft.colors.BLACK,
        border_radius=10,
        width=cnt_superior.width * 0.80,
        hint_text="Informe a cidade e o pais ",
        hint_style=ft.TextStyle(
            size=12,
            color=ft.colors.BLUE_GREY,
            ),
        text_align=ft.TextAlign.CENTER,
        text_style=ft.TextStyle(
            size=14,
            color=ft.colors.BLACK,
            weight=ft.FontWeight.BOLD,
            ),
        value=" Rio de Janeiro, RJ",
        )
    
    botao_pesquisa = ft.IconButton(
        icon= ft.icons.SEARCH,
        icon_color=ft.colors.BLACK,
        on_click=update_climate,
    )

    cnt_superior.content.controls.append(pesquisa_local)
    cnt_superior.content.controls.append(botao_pesquisa)

    #---------------------------------------------------------------------------------
    # Container central:

    cnt_central = ft.Container(
        #bgcolor= ft.colors.GREY_100,
        height = 200,
        width= cnt_principal.width * 0.95,
        content= ft.Column(

        )
    )

    cnt_central_linha1 = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Text(
                value="cidade",
                font_family="Segaon Medium",
                color=ft.colors.BLACK,
                size=38,
                weight=ft.FontWeight.BOLD,
            )
        ]
    )
    
    cnt_central_linha2 = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Image(
                src="https://cdn-icons-png.flaticon.com/512/5538/5538361.png",
                width=100,
                height=100,
            )
        ]
    )
    cnt_central_linha3 = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Text(
                value="17°",
                font_family="Segaon Medium",
                color=ft.colors.BLACK,
                size=28,
                weight=ft.FontWeight.BOLD,
                
            )
        ]
    )
    cnt_central_linha4 = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Text(
                value="75%",
                font_family="Segaon Medium",
                color=ft.colors.BLACK,
                weight=ft.FontWeight.BOLD,
                
                
            )
        ]
    )

    cnt_central.content.controls.append(cnt_central_linha1)
    cnt_central.content.controls.append(cnt_central_linha2)
    cnt_central.content.controls.append(cnt_central_linha3)
    cnt_central.content.controls.append(cnt_central_linha4)
    #---------------------------------------------------------------------------------
    # Container inferior:
    
    cnt_inferior = ft.Container(
        #bgcolor= ft.colors.GREY_100,
        height = 150,
        content= ft.Column(

        )
    )

    cnt_inferior_linha1 = ft.Row(
        alignment=ft.MainAxisAlignment.SPACE_AROUND,
        controls=[
            ft.Text(
                f"D{i}",
                color=ft.colors.BLACK,
                font_family="Segaon Medium",
                weight=ft.FontWeight.BOLD,
                
            ) for i in range(1,6) # função de repetição, faz com que ele repita o texto 5 vezes substituindo o I.
            
        ],
    )

    cnt_inferior_linha2 = ft.Row(
        alignment=ft.MainAxisAlignment.SPACE_AROUND,
        controls=[
            ft.Image(
                src="https://cdn-icons-png.flaticon.com/512/5538/5538361.png",
                width=50,
                height=50,
            ) for i in range(1,6)
        ]
    )

    cnt_inferior_linha3 = ft.Row(
        alignment=ft.MainAxisAlignment.SPACE_AROUND,
        controls=[
            ft.Text(
                f"T{i}",
                color=ft.colors.BLACK,
                font_family="Segaon Medium",
                weight=ft.FontWeight.BOLD,
                
            ) for i in range(1,6) # função de repetição, faz com que ele repita o texto 5 vezes substituindo o I.
            
        ],
    )

    cnt_inferior.content.controls.append(cnt_inferior_linha1)
    cnt_inferior.content.controls.append(cnt_inferior_linha2)
    cnt_inferior.content.controls.append(cnt_inferior_linha3)
    #---------------------------------------------------------------------------------

    # Adicionando os containers dentro do container principal
    cnt_principal.content.controls.append(cnt_superior)
    cnt_principal.content.controls.append(cnt_central)
    cnt_principal.content.controls.append(cnt_inferior)

    
    
    page.add(
        cnt_principal,
        )
    get_user_location(None)

ft.app(port=8550, target=main, view=ft.AppView.FLET_APP)