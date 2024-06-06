import pyglet
# -----------Variables de colores--------
text_white = "#FFFFFF"
text_black = "#000000"
bg_white = "#FFFFFF"
bg_light_blue = "#B8CEE4"
bg_blue = "#034EB7"
bg_dark = "#161616"
blue_button = "#0575E6"
black_button = "#000000"
bg_gray_light = "#EBEBEB"


# ---------variables de fuentes----------------
# añadiendo fuentes
pyglet.font.add_file("fuentes/candal.ttf")
pyglet.font.add_file("fuentes/amaranth.ttf")
pyglet.font.add_file("fuentes/average.ttf")
pyglet.font.add_file("fuentes/amiri.ttf")
#----------------------------------------------
font_text_bold = ("candal", 40) 
font_text_bold_medium = ("candal", 32)
font_text_bold_small = ("candal", 24)
#---------------------------------------
font_text_amaranth = ("amaranth", 32)
font_text_amaranth_medium = ("amaranth", 28)
font_text_amaranth_small = ("amaranth", 18)
# --------------------------------------------
font_text_regular = ("amiri", 24)
font_text_regular_medium = ("amiri", 18)
font_text_regular_small = ("amiri", 14)
# -------------------------------------------
font_text_entry = ("average", 16)
font_text_button = ("amaranth", 18)