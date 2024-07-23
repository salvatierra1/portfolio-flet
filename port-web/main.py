import flet as ft

def main(page: ft.Page):

    page.scroll=True
    
    def view_inicio(e):
        page.clean()
        page.add(inicio)
        page.update()
    
    def view_sobre_mi(e):
        page.clean()
        page.add(sobre_mi)
        page.update()
    
    def view_trabajos(e):
        page.clean()
        page.add(trabajos)
        page.update()
    
    def view_contacto(e):
        page.clean()
        page.add(contacto)
        page.update()
    
    # Navegación
    page.appbar = ft.AppBar(
        leading_width=40,
        title = ft.CircleAvatar(
        content=ft.Text("LP"),
        color="yellow",
        bgcolor="blue300"
        ),
        center_title=False,
        bgcolor=ft.colors.WHITE,
        actions=[
            ft.PopupMenuButton(
                items=[
                    ft.PopupMenuItem(text="Inicio", on_click=view_inicio),
                    ft.PopupMenuItem(),
                    ft.PopupMenuItem(text="Sobre mi", on_click=view_sobre_mi),
                    ft.PopupMenuItem(text="Trabajos", on_click=view_trabajos),
                    ft.PopupMenuItem(text="Contacto", on_click=view_contacto),
                ],
                icon_color="black"
            ),
        ],
    )
    
    # Inicio
    inicio = ft.Container(
        content=ft.ResponsiveRow(
            [ft.Container(                    
                    content=ft.Column(
                        [
                            ft.Text(
                                spans=[
                                    ft.TextSpan(
                                        "PAREDES, LEO",
                                        ft.TextStyle(
                                            size=40,
                                            weight="Bold",
                                            foreground=ft.Paint(
                                                gradient=ft.PaintLinearGradient(
                                                    (60, 50), (150, 20), [ft.colors.BLUE, ft.colors.YELLOW]
                                                )
                                            ),
                                        ),
                                    ),
                                ],
                            ),
                            ft.Divider(),
                            ft.Text("Jugador Profesional de Fútbol", size=20),
                            ft.Row([
                                ft.TextButton(content=ft.Image(src="whatsapp.png", width=30, height=30, tooltip="Image Tooltip"),width=50, height=50),
                                ft.TextButton(content=ft.Image(src="instagram.png", width=30, height=30, tooltip="Image Tooltip"), width=50, height=50),
                                ft.TextButton(content=ft.Image(src="facebook.png", width=30, height=30, tooltip="Image Tooltip"), width=50, height=50),
                                ]
                            )
                        ]),
                    padding=5,
                    col={"sm": 12, "md": 12, "xl": 12}
                ),
            ]
        ),
        padding=10,
        margin=50,
        border_radius=15,
    )
    
    # SobreMi
    sobre_mi = ft.Container(
        content=ft.ResponsiveRow(
            [ft.Container(                    
                    content=ft.Column(
                        [
                            ft.Text(
                                spans=[
                                    ft.TextSpan(
                                        "SOBRE MÍ",
                                        ft.TextStyle(
                                            size=40,
                                            weight="Bold",
                                            foreground=ft.Paint(
                                                gradient=ft.PaintLinearGradient(
                                                    (60, 50), (150, 20), [ft.colors.BLUE, ft.colors.WHITE]
                                                )
                                            ),
                                        ),
                                    ),
                                ],
                            ),
                            ft.Divider(color="blue"),
                            ft.Card(
                                content=ft.Container(
                                    content=ft.Column(
                                        [
                                            ft.Text("Leandro Paredes nació el 29 de junio de 1994 en San Justo, una localidad ubicada en el área metropolitana de Buenos Aires, a 2,5 km del acceso oeste a la capital argentina Su padre es argentino y su madre es paraguaya. Su aventura en el fútbol inició a la edad de 3 años en un club de baby fútbol llamado La Justina de San Justo. También jugaba en el club San Pantaleon, en La Tablada. Cuando su familia se mudó al barrio porteño de Mataderos, pasó a jugar al Brisas del Sur, otro club de baby de la ciudad donde nació.",color="black", size=20, text_align="justify"),

                                        ]
                                    ),
                                    padding=10,
                                    border_radius=10,
                                    bgcolor="white",
                                ),
                                col={"sm": 12, "md": 12, "xl": 12}
                            ),
                        ]),
                    padding=5,
                    col={"sm": 12, "md": 12, "xl": 12}
                ),
            ]
        ),
        padding=10,
        margin=50,
        border_radius=15,
    )
    
    # Trabajos
    trabajos = ft.Container(
        content=ft.ResponsiveRow(
            [
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text(
                                spans=[
                                    ft.TextSpan(
                                        "TRABAJOS",
                                        ft.TextStyle(
                                            size=40,
                                            weight="Bold",
                                            foreground=ft.Paint(
                                                gradient=ft.PaintLinearGradient(
                                                    (60, 50), (150, 20), [ft.colors.BLUE, ft.colors.WHITE]
                                                )
                                            ),
                                        ),
                                    ),
                                ],
                            ),
                            ft.Divider(color="blue"),
                        ]
                    ),
                    padding=5,
                    col={"sm": 12, "md": 12, "xl": 12}
                ),
                ft.Container(
                    content=ft.ResponsiveRow(
                        [
                            ft.Card(
                                content=ft.Container(
                                    content=ft.Column(
                                        [
                                            ft.ListTile(
                                                leading=ft.Icon(ft.icons.ALBUM_OUTLINED, color="blue"),
                                                title=ft.Text("Sistema de Gestión de Estudiantes", color="Black", size=15, weight="bold"),
                                                subtitle=ft.Text(
                                                    "Un Sistema de Gestión de Estudiantes (SGE) es una plataforma integral diseñada para facilitar y optimizar la administración académica en instituciones educativas. Este sistema permite gestionar de manera eficiente la información relacionada con los estudiantes, desde su inscripción hasta su graduación.",
                                                    text_align="justify", color="Black"
                                                ),
                                            ),
                                            ft.Row(
                                                [ft.IconButton(icon=ft.icons.CODE, bgcolor="Blue")],
                                                alignment=ft.MainAxisAlignment.END,
                                            ),
                                        ]
                                    ),
                                    width=400,
                                    padding=10,
                                    bgcolor="white",
                                    border_radius=10
                                ),
                                col={"sm": 12, "md": 6, "xl": 4}
                            ),
                            ft.Card(
                                content=ft.Container(
                                    content=ft.Column(
                                        [
                                            ft.ListTile(
                                                leading=ft.Icon(ft.icons.ALBUM_OUTLINED, color="blue"),
                                                title=ft.Text("Sistema de Gestión de Estudiantes", color="Black", size=15, weight="bold"),
                                                subtitle=ft.Text(
                                                    "Un Sistema de Gestión de Estudiantes (SGE) es una plataforma integral diseñada para facilitar y optimizar la administración académica en instituciones educativas. Este sistema permite gestionar de manera eficiente la información relacionada con los estudiantes, desde su inscripción hasta su graduación.",
                                                    text_align="justify", color="Black"
                                                ),
                                            ),
                                            ft.Row(
                                                [ft.IconButton(icon=ft.icons.CODE, bgcolor="Blue")],
                                                alignment=ft.MainAxisAlignment.END,
                                            ),
                                        ]
                                    ),
                                    width=400,
                                    padding=10,
                                    bgcolor="white",
                                    border_radius=10
                                ),
                                col={"sm": 12, "md": 6, "xl": 4}
                            ),
                            ft.Card(
                                content=ft.Container(
                                    content=ft.Column(
                                        [
                                            ft.ListTile(
                                                leading=ft.Icon(ft.icons.ALBUM_OUTLINED, color="blue"),
                                                title=ft.Text("Sistema de Gestión de Estudiantes", color="Black", size=15, weight="bold"),
                                                subtitle=ft.Text(
                                                    "Un Sistema de Gestión de Estudiantes (SGE) es una plataforma integral diseñada para facilitar y optimizar la administración académica en instituciones educativas. Este sistema permite gestionar de manera eficiente la información relacionada con los estudiantes, desde su inscripción hasta su graduación.",
                                                    text_align="justify", color="Black"
                                                ),
                                            ),
                                            ft.Row(
                                                [ft.IconButton(icon=ft.icons.CODE, bgcolor="Blue")],
                                                alignment=ft.MainAxisAlignment.END,
                                            ),
                                        ]
                                    ),
                                    width=400,
                                    padding=10,
                                    bgcolor="white",
                                    border_radius=10
                                ),
                                col={"sm": 12, "md": 6, "xl": 4}
                            ),
                        ],
                        col={"sm": 12, "md": 12, "xl": 12}
                    )
                )
            ]
        ),
        padding=10,
        margin=50,
        border_radius=15,
    )
    
    # Contacto
    contacto = ft.Container(
        content=ft.ResponsiveRow(
            [
                ft.Container(
                    content=ft.Column(
                        [
                            ft.Text(
                                spans=[
                                    ft.TextSpan(
                                        "CONTACTO",
                                        ft.TextStyle(
                                            size=40,
                                            weight="Bold",
                                            foreground=ft.Paint(
                                                gradient=ft.PaintLinearGradient(
                                                    (60, 50), (150, 20), [ft.colors.BLUE, ft.colors.WHITE]
                                                )
                                            ),
                                        ),
                                    ),
                                ],
                            ),
                            ft.Divider(color="blue"),
                        ]
                    ),
                    padding=5,
                    col={"sm": 12, "md": 12, "xl": 12}
                ),
                ft.Container(
                    content=ft.ResponsiveRow(
                        [
                            ft.Card(
                                content=ft.Container(
                                    content=ft.Column(
                                        [   ft.Text("Redes sociales:", size=20, weight="bold", color="black"),
                                            ft.Divider(),
                                            ft.Row(
                                                [
                                                    ft.TextButton(content=ft.Image(src="instagram.png", width=32, height=32, tooltip="Image Tooltip")),
                                                    ft.TextButton(content=ft.Image(src="linkedin.png", width=32, height=32, tooltip="Image Tooltip")),
                                                    ft.TextButton(content=ft.Image(src="facebook.png", width=32, height=32, tooltip="Image Tooltip")),
                                                ]

                                            ) 
                                        ]
                                    ),
                                    width=400,
                                    padding=10,
                                    border_radius=10,
                                    bgcolor="white",
                                ),
                                col={"sm": 6, "md": 6, "xl": 6}
                            ),
                            ft.Card(
                                content=ft.Container(
                                    content=ft.Column(
                                        [   ft.Text("Correo Electrónico:", size=20, weight="bold", color="black"),
                                            ft.Divider(),
                                            ft.Row(
                                                [
                                                    ft.TextButton("leoparedes5@gmail.com", icon=ft.icons.MAIL, icon_color="Black", 
                                                        style=ft.ButtonStyle(
                                                        color="black",
                                                    ),),
                                                ]
                                            ) 
                                        ]
                                    ),
                                    width=400,
                                    padding=10,
                                    border_radius=10,
                                    bgcolor="white",
                                ),
                                col={"sm": 6, "md": 6, "xl": 6}
                            ),
                        ],
                        col={"sm": 12, "md": 12, "xl": 12}
                    )
                )
            ]
        ),
        padding=10,
        margin=50,
        border_radius=15,
    )
  
    page.padding = 0
    page.add(inicio)
    
ft.app(target=main)