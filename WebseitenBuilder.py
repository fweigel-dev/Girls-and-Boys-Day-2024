WebseitenParser: list = []


####################
# Add new elements #
####################

def text(text: str):
    WebseitenParser.append(
        {"type": "text", "text": text, "size": 24, "color": "#000000", "position_x": "0", "position_y": "0",
         "font": "Arial", "weight": "400"})


def bild(url: str):
    WebseitenParser.append(
        {"type": "image", "url": url, "position_x": "0", "position_y": "0", "size_x": "100", "size_y": "100"})


def video(url: str):
    WebseitenParser.append(
        {"type": "video", "url": url, "position_x": "0", "position_y": "0", "size_x": "100", "size_y": "100"})


def titel(title: str):
    WebseitenParser.append({"type": "title", "title": title})


def icon(url: str):
    WebseitenParser.append({"type": "icon", "icon": url})


def hintergrundbild(url: str):
    WebseitenParser.append({"type": "background-image", "url": url, "repeat": "repeat", "size": "cover"})


def hintergrundfarbe(farbe: str):
    WebseitenParser.append({"type": "background-color", "background-color": farbe})


def breiter():
    if "size_x" in WebseitenParser[-1]:
        WebseitenParser[-1]["size_x"] = str(int(WebseitenParser[-1]["size_x"]) + 10)
    else:
        print(
            "\033[31m" + "Achtung: Du versuchst die Breite zu ändern, bei einem Element, welches keine Breite hat!" + "\033[0m")


def schmaler():
    if "size_x" in WebseitenParser[-1]:
        WebseitenParser[-1]["size_x"] = str(int(WebseitenParser[-1]["size_x"]) - 10)
    else:
        print(
            "\033[31m" + "Achtung: Du versuchst die Breite zu ändern, bei einem Element, welches keine Breite hat!" + "\033[0m")


def hoeher():
    if "size_y" in WebseitenParser[-1]:
        WebseitenParser[-1]["size_y"] = str(int(WebseitenParser[-1]["size_y"]) + 10)
    else:
        print(
            "\033[31m" + "Achtung: Du versuchst die Höhe zu ändern, bei einem Element, welches keine Höhe hat!" + "\033[0m")


def tiefer():
    if "size_y" in WebseitenParser[-1]:
        WebseitenParser[-1]["size_y"] = str(int(WebseitenParser[-1]["size_y"]) - 10)
    else:
        print(
            "\033[31m" + "Achtung: Du versuchst die Höhe zu ändern, bei einem Element, welches keine Höhe hat!" + "\033[0m")


def links():
    if "position_y" in WebseitenParser[-1]:
        WebseitenParser[-1]["position_y"] = str(int(WebseitenParser[-1]["position_y"]) - 250)
        if int(WebseitenParser[-1]["position_y"]) < 0:
            print("\033[31m" + "Achtung: Du verschiebst ein Element links außerhalb die Seite!" + "\033[0m")
    else:
        print("\033[31m" + "Achtung: Du versuchst ein Element zu verschieben, welches keine Position hat!" + "\033[0m")


def rechts():
    if "position_y" in WebseitenParser[-1]:
        WebseitenParser[-1]["position_y"] = str(int(WebseitenParser[-1]["position_y"]) + 250)
    else:
        print("\033[31m" + "Achtung: Du versuchst ein Element zu verschieben, welches keine Position hat!" + "\033[0m")


def oben():
    if "position_x" in WebseitenParser[-1]:
        WebseitenParser[-1]["position_x"] = str(int(WebseitenParser[-1]["position_x"]) - 100)
        if int(WebseitenParser[-1]["position_x"]) < 0:
            print("\033[31m" + "Achtung: Du verschiebst ein Element über die Seite!" + "\033[0m")
    else:
        print("\033[31m" + "Achtung: Du versuchst ein Element zu verschieben, welches keine Position hat!" + "\033[0m")


def unten():
    if "position_x" in WebseitenParser[-1]:
        WebseitenParser[-1]["position_x"] = str(int(WebseitenParser[-1]["position_x"]) + 100)
    else:
        print("\033[31m" + "Achtung: Du versuchst ein Element zu verschieben, welches keine Position hat!" + "\033[0m")


def textgroesser():
    if "size" in WebseitenParser[-1]:
        WebseitenParser[-1]["size"] = str(int(WebseitenParser[-1]["size"]) + 10)
    else:
        print(
            "\033[31m" + "Achtung: Du versuchst die Schriftgröße zu ändern, bei einem Element, welches keine Schriftgröße hat!" + "\033[0m")


def textkleiner():
    if "size" in WebseitenParser[-1]:
        WebseitenParser[-1]["size"] = str(int(WebseitenParser[-1]["size"]) - 10)
    else:
        print(
            "\033[31m" + "Achtung: Du versuchst die Schriftgröße zu ändern, bei einem Element, welches keine Schriftgröße hat!" + "\033[0m")


def farbe(farbe: str):
    if "color" in WebseitenParser[-1]:
        WebseitenParser[-1]["color"] = farbe
    else:
        print(
            "\033[31m" + "Achtung: Du versuchst die Farbe zu ändern, bei einem Element, welches keine Farbe hat!" + "\033[0m")


def textdicker():
    if "weight" in WebseitenParser[-1]:
        WebseitenParser[-1]["weight"] = str(int(WebseitenParser[-1]["weight"]) + 200)
        if int(WebseitenParser[-1]["weight"]) > 1000:
            print(
                "\033[31m" + "Achtung: Du versuchst die Text Dicke zu ändern, bei einem Element, welches schon die "
                             "maximale Breite hat!" + "\033[0m")
            WebseitenParser[-1]["weight"] = "1000"
    else:
        print(
            "\033[31m" + "Achtung: Du versuchst die Breite zu ändern, bei einem Element, welches keine Text Dicke hat!"
            + "\033[0m")


def textduenner():
    if "weight" in WebseitenParser[-1]:
        WebseitenParser[-1]["weight"] = str(int(WebseitenParser[-1]["weight"]) - 200)
        if int(WebseitenParser[-1]["weight"]) < 100:
            print(
                "\033[31m" + "Achtung: Du versuchst die Text Dicke zu verkleinern, bei einem Element, welches schon die "
                             "minimale Breite hat!" + "\033[0m")
            WebseitenParser[-1]["weight"] = "100"
    else:
        print(
            "\033[31m" + "Achtung: Du versuchst die Breite zu ändern, bei einem Element, welches keine Text Dicke hat!"
            + "\033[0m")


############################
# Modify existing elements #
############################


def verschieben_nach_unten(pixel: int):
    last_element: dict = get_last_element()
    if last_element["type"] == "text" or last_element["type"] == "image" or last_element["type"] == "video":
        last_element["position_x"] = str(int(last_element["position_x"]) + pixel)
    else:
        log_error(
            f"Du hast versucht, ein Element vom Typ **{last_element['type']}** zu verschieben. Dieser Typ kann nicht "
            f"verschoben werden!\n"
            f"  Du kannst die Methode `verschieben_nach_unten` nur direkt nach Texten, Bildern und Videos benutzen!")


def verschieben_nach_oben(pixel: int):
    last_element: dict = get_last_element()
    if last_element["type"] == "text" or last_element["type"] == "image" or last_element["type"] == "video":
        last_element["position_x"] = str(int(last_element["position_x"]) - pixel)
    else:
        log_error(
            f"Du hast versucht, ein Element vom Typ **{last_element['type']}** zu verschieben. Dieser Typ kann nicht "
            f"verschoben werden!\n"
            f"  Du kannst die Methode `verschieben_nach_oben` nur direkt nach Texten, Bildern und Videos benutzen!")


def verschieben_nach_rechts(pixel: int):
    last_element: dict = get_last_element()
    if last_element["type"] == "text" or last_element["type"] == "image" or last_element["type"] == "video":
        last_element["position_y"] = str(int(last_element["position_y"]) + pixel)
    else:
        log_error(
            f"Du hast versucht, ein Element vom Typ **{last_element['type']}** zu verschieben. Dieser Typ kann nicht "
            f"verschoben werden!\n"
            f"  Du kannst die Methode `verschieben_nach_rechts` nur direkt nach Texten, Bildern und Videos benutzen!")


def verschieben_nach_links(pixel: int):
    last_element: dict = get_last_element()
    if last_element["type"] == "text" or last_element["type"] == "image" or last_element["type"] == "video":
        last_element["position_y"] = str(int(last_element["position_y"]) - pixel)
    else:
        log_error(
            f"Du hast versucht, ein Element vom Typ **{last_element['type']}** zu verschieben. Dieser Typ kann nicht "
            f"verschoben werden!\n"
            f"  Du kannst die Methode `verschieben_nach_links` nur direkt nach Texten, Bildern und Videos benutzen!")


def bild_breite(pixel: str):
    last_element: dict = get_last_element()
    if last_element["type"] == "image":
        last_element["size_x"] = pixel
    else:
        log_error(
            f"Du hast versucht, ein Element vom Typ **{last_element['type']}** zu verändern. Dieser Typ kann nicht "
            f"verändert werden!\n"
            f"  Du kannst die Methode `bild_breite` nur direkt nach Bildern benutzen!")


def bild_hoehe(pixel: str):
    last_element: dict = get_last_element()
    if last_element["type"] == "image":
        last_element["size_y"] = pixel
    else:
        log_error(
            f"Du hast versucht, ein Element vom Typ **{last_element['type']}** zu verändern. Dieser Typ kann nicht "
            f"verändert werden!\n"
            f"  Du kannst die Methode `bild_hoehe` nur direkt nach Bildern benutzen!")


##################
# Util functions #
##################

def get_last_element():
    return WebseitenParser[-1]


##########################
# Generate Error Message #
##########################

def log_error(message: str):
    formatted_message = (
            "\n\033[1m\033[97m\033[41m"
            "+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+\n"
            "  ACHTUNG: In deinem Code ist ein Fehler aufgetreten.\n" +
            f"  {message}\n"
            "+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+\n\033[0m"
    )
    raise Exception(formatted_message)


#################
# Generate HTML #
#################


def collect_html_preset_information(website_parser: list):
    title: str = "Meine eigene Webseite"
    icon: str = "https://www.united-internet.de/favicon.ico"
    background_image: str = ""
    background_repeat: str = "repeat"
    background_size: str = "cover"
    background_color: str = "#ffffff"

    for json in website_parser:
        if json["type"] == "title":
            title = json["title"]
        elif json["type"] == "icon":
            icon = json["icon"]
        elif json["type"] == "background-image":
            background_image = json["url"]
            background_repeat = json["repeat"]
            background_size = json["size"]
        elif json["type"] == "background-color":
            background_color = json["background-color"]

    return generate_html_preset_start(title, icon, background_image, background_repeat, background_size,
                                      background_color)


def generate_html_preset_start(title: str, icon: str, background_image: str, background_repeat: str,
                               background_size: str,
                               background_color: str):
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


def parse_text_images_videos(json: dict):
    if json["type"] == "text":
        return f"\n<p style=\"font-size: {json['size']}px; color: {json['color']}; position: absolute; top: {json['position_x']}px; left: {json['position_y']}px; font-family: {json['font']},serif; font-weight: {json['weight']};\">{json['text']}</p>"
    elif json["type"] == "image":
        return f"\n<img src=\"{json['url']}\" style=\"position: absolute; top: {json['position_x']}px; left: {json['position_y']}px; width: {json['size_x']}%; height: {json['size_y']}%;\" alt="">"
    elif json["type"] == "video":
        return f'\n<iframe style="position:relative; top:{json["position_x"]}px; left: {json["position_y"]}px; width: {json["size_x"]}%; height: {json["size_y"]}%;" src="{json["url"]}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>'


def bauen():
    print("Webseite wird erstellt...")
    print(WebseitenParser)
    with open("index.html", "w") as file:
        print("Datei wird erstellt...")
        file.write(collect_html_preset_information(WebseitenParser))
        for parser in WebseitenParser:
            if parser["type"] == "text" or parser["type"] == "image" or parser["type"] == "video":
                file.write(parse_text_images_videos(parser))
        file.write(generate_html_preset_end())
        print("Webseite wurde erstellt!")
