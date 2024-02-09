WebseitenParser: list = []


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
        return f"\n<video src=\"{json['url']}\" style=\"position: absolute; top: {json['position_x']}px; left: {json['position_y']}px; width: {json['size_x']}%; height: {json['size_y']}%;\"></video>"


def bauen():
    print(WebseitenParser)
    print("Webseite wird erstellt...")
    with open("index.html", "w") as file:
        print("Datei wird erstellt...")
        file.write(collect_html_preset_information(WebseitenParser))
        for parser in WebseitenParser:
            if parser["type"] == "text" or parser["type"] == "image" or parser["type"] == "video":
                file.write(parse_text_images_videos(parser))
        file.write(generate_html_preset_end())
