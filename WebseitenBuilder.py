WebseitenParser: list = []


def generate_html_preset_start(title: str = "Meine eigene Webseite",
                               icon: str = "https://www.united-internet.de/favicon.ico",
                               background_image: str = "",
                               background_repeat: str = "repeat",
                               background_size: str = "cover",
                               background_color: str = "#ffffff"):
    if background_image != "":
        background_image = f"\n            background-image: url(\"{background_image}\");"

    background_repeat = f"background-repeat: {background_repeat};"
    background_size = f"background-size: {background_size};"
    background_color = f"background-color: {background_color};"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <link rel="icon" type="image/png" href="{icon}">
    <style>
        body {{{background_image}
            {background_repeat}
            {background_size}
            {background_color}
        }}
    </style>
</head>
<body>"""


def generate_html_preset_end():
    return """
</body>
</html>"""


def bauen():
    print("Webseite wird erstellt...")
    with open("index.html", "w") as file:
        print("Datei wird erstellt...")
        file.write(generate_html_preset_start())
        for parser in WebseitenParser:
            file.write(parser)
        file.write(generate_html_preset_end())


bauen()