from PIL import Image, ImageDraw, ImageFont
import os

def generate_card(title, artist, duration, requester, cover_path='default.jpg'):
    card_width, card_height = 1280, 720
    background = Image.new("RGB", (card_width, card_height), "#111111")
    cover = Image.open(cover_path).convert("RGB").resize((400, 400))
    background.paste(cover, (80, 160))
    draw = ImageDraw.Draw(background)
    font_title = ImageFont.truetype("arial.ttf", 60)
    font_sub = ImageFont.truetype("arial.ttf", 40)
    font_small = ImageFont.truetype("arial.ttf", 35)
    bar_x, bar_y = 550, 540
    bar_w, bar_h = 650, 18
    draw.rounded_rectangle([bar_x, bar_y, bar_x + bar_w, bar_y + bar_h], radius=9, fill="#444444")
    draw.rounded_rectangle([bar_x, bar_y, bar_x + 80, bar_y + bar_h], radius=9, fill="#1DB954")
    draw.text((550, 160), "Now Playing", font=font_small, fill="#888888")
    draw.text((550, 210), title, font=font_title, fill="white")
    draw.text((550, 300), f"Artist: {artist}", font=font_sub, fill="#CCCCCC")
    draw.text((550, 370), f"Duration: {duration}", font=font_sub, fill="#CCCCCC")
    draw.text((550, 440), f"Requested by: {requester}", font=font_sub, fill="#1DB954")
    os.makedirs("generated", exist_ok=True)
    output_path = "generated/current_song.jpg"
    background.save(output_path)
    return output_path
