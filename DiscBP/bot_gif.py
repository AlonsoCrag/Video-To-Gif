from flask import Blueprint, request
from CV.insert_text import TextIntoGif
from CV.movie import BorderVideo
from CV.cvFunc import TransformVideo

DiscordBluePrint = Blueprint('discord_route', __name__)

@DiscordBluePrint.route('/discord', methods = ['POST', 'GET'])
def Route():
    print("REQUEST IN /discord allowed")
    Username = request.json["username"]
    TextIntoGif(Username)
    BorderVideo(Username)
    TransformVideo(f'./Output_Img/{Username}.mp4', Username)
    return "GG, /discord is running all good xD"