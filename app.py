from linebot.models import *
from linebot import (LineBotApi, WebhookHandler, HttpClient, RequestsHttpClient)
from linebot.exceptions import (InvalidSignatureError, LineBotApiError)
from linebot.models.actions import RichMenuSwitchAction
from linebot.models.rich_menu import RichMenuAlias
from flask import Flask, request, abort, send_from_directory
from argparse import ArgumentParser
from werkzeug.middleware.proxy_fix import ProxyFix
from urllib.parse import urlencode
from datetime import datetime
import requests as uReq
import requests, json, errno, os, sys, random, tempfile, datetime, urllib
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom, Joined,
    TemplateSendMessage, ConfirmTemplate, MessageAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URIAction,
    PostbackAction, DatetimePickerAction, UnsendEvent,
    CameraAction, CameraRollAction, LocationAction, MemberIds,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
    MemberJoinedEvent, MemberLeftEvent,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, IconComponent, ButtonComponent,
    SeparatorComponent, QuickReply, QuickReplyButton,
    ImageSendMessage, VideoSendMessage, AudioSendMessage,
    RichMenu, RichMenuArea, RichMenuSize, RichMenuBounds,
)
app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_host=1, x_proto=1)
line_bot_api = LineBotApi('ks/r5d+zVhMhzF3NhX2Ru1pkagDJVZtEgD1twVOIrFeCvkaQFYHFTy4yYTP2l7zzRa8p8WnyXsCnzegpcd/WC3Dv11LeLprRTdA/HnESJHHK2bKgPQQFwrmWX3Wr+lArkAJNnPJDO/980tDuMo7H2wdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('89c44971d85f42f346c60755f3ec7fad')
Xeberlhyn = line_bot_api
chanels = Xeberlhyn.get_bot_info()
BotMID = chanels.user_id
Creator = 'u7b53d142b0b84803853f8841e48cba82'
notes = {}
msg_dict = {}
tym = datetime.datetime.now()
vst = {
    "template": True,
}

#____________dev_________________
def sendMessage(to, teks):
    return Xeberlhyn.reply_message(to, TextSendMessage(text=teks))

def sendImage(to, url):
    app.logger.info("url=" + url)
    return Xeberlhyn.reply_message(to, ImageSendMessage(url, url))

def sendAudio(to, url):
    app.logger.info("url=" + url)
    return Xeberlhyn.reply_message(to, AudioSendMessage(url, 60000))

def sendVideo(to, url):
    app.logger.info("url=" + url)
    preview = "https://i.ibb.co/wrJNNGL/20220219-100319.jpg"
    return Xeberlhyn.reply_message(to, VideoSendMessage(url, preview))

def sendTextImageURL(to, teks, url):
    app.logger.info("url=" + url)
    return Xeberlhyn.reply_message(to, [TextSendMessage(text=teks), ImageSendMessage(url, url)])

def sendTextAudioURL(to, teks, url):
    app.logger.info("url=" + url)
    return Xeberlhyn.reply_message(to, [TextSendMessage(text=teks), AudioSendMessage(url, 60000)])

def sendTextVideoURL(to, teks, url):
    app.logger.info("url=" + url)
    preview = "https://i.ibb.co/wrJNNGL/20220219-100319.jpg"
    return Xeberlhyn.reply_message(to, [TextSendMessage(text=teks), VideoSendMessage(url, preview)])

def sendFlexVideoURL(to, data, url):
    app.logger.info("url=" + url)
    preview = "https://i.ibb.co/wrJNNGL/20220219-100319.jpg"
    return Xeberlhyn.reply_message(to, [FlexSendMessage(alt_text="©VTEAM-OFFICIAL", contents=data), VideoSendMessage(url, preview)])

def sendFlexAudioURL(to, data, url):
    app.logger.info("url=" + url)
    return Xeberlhyn.reply_message(to, [FlexSendMessage(alt_text="©VTEAM-OFFICIAL", contents=data), VideoSendMessage(url, 60000)])

def sendFlexImageURL(to, data, url):
    app.logger.info("url=" + url)
    return Xeberlhyn.reply_message(to, [FlexSendMessage(alt_text="©VTEAM-OFFICIAL", contents=data), VideoSendMessage(url, url)])

def sendDowbleMessage(to, txt1, txt2):
    return Xeberlhyn.reply_message(to, [TextSendMessage(text=txt1), TextSendMessage(text=txt2)])

#____________Def programing__________
@handler.add(MemberJoinedEvent)
def handle_member_joined(event):
    to = event.reply_token
    room = event.source.group_id
    G = Xeberlhyn.get_group_summary(room)
    url = G.picture_url
    name = G.group_name
    data = { "type": "carousel", "contents": [ { "type": "bubble", "size": "micro", "body": { "borderWidth": "medium", "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://i.ibb.co/XJgtjWQ/ezgif-com-gif-to-apng-2022-02-03-T111625-179.png", "position": "absolute", "aspectMode": "cover", "offsetTop": "0px", "offsetBottom": "0px", "offsetStart": "0px", "offsetEnd": "0px", "size": "full", "aspectRatio": "2:3", "backgroundColor": "#8A2BE2cc", "animated": True }, { "contents": [ { "contents": [ { "contents": [ { "contents": [ { "url": "https://i.ibb.co/VjBvDF9/ezgif-com-gif-to-apng-29.png", "size": "full", "type": "image", "animated": True, "aspectMode": "cover" } ], "type": "box", "layout": "vertical", "borderColor": "#FFB6C1", "cornerRadius": "sm", "borderWidth": "normal" }, { "contents": [ { "type": "text", "text": "WELCOME MESSAGE", "size": "xxs", "align": "center", "color": "#00FFFF", "weight": "bold" }, { "contents": [ { "contents": [ { "type": "text", "text": "sains from imajination", "size": "xxs", "align": "center", "color": "#7CFC00", "weight": "bold", "style": "italic", "decoration": "underline" } ], "type": "box", "layout": "vertical", "flex": 4, "borderWidth": "light", "borderColor": "#FF0000", "cornerRadius": "lg" } ], "type": "box", "layout": "horizontal" } ], "type": "box", "layout": "vertical", "flex": 4 } ], "type": "box", "layout": "horizontal", "borderWidth": "medium", "borderColor": "#0000FF", "cornerRadius": "sm" }, { "contents": [ { "contents": [ { "contents": [ { "type": "image", "url": "https://i.ibb.co/JkQx1vY/ezgif-com-gif-to-apng-2022-02-03-T103541-832.png", "position": "absolute", "size": "full", "aspectRatio": "30:90", "aspectMode": "cover", "animated": True }, { "contents": [ { "type": "text", "text": "⭐", "size": "xxs", "color": "#FFD700", "align": "center" } ], "type": "box", "layout": "vertical" }, { "contents": [ { "type": "text", "text": "💠", "size": "xxs", "color": "#FFD700", "align": "center" } ], "type": "box", "layout": "vertical" }, { "contents": [ { "type": "text", "text": "💠", "size": "xxs", "color": "#FFD700", "align": "center" } ], "type": "box", "layout": "vertical" } ], "type": "box", "layout": "vertical", "borderWidth": "normal", "width": "20px", "height": "56px", "alignItems": "center", "justifyContent": "center" }, { "contents": [ { "contents": [ { "type": "text", "text": "⏩", "size": "xxs", "color": "#FFD700", "align": "center" } ], "type": "box", "layout": "vertical" } ], "type": "box", "layout": "vertical", "borderWidth": "normal" }, { "contents": [ { "type": "image", "url": "https://i.ibb.co/JkQx1vY/ezgif-com-gif-to-apng-2022-02-03-T103541-832.png", "position": "absolute", "size": "full", "aspectRatio": "30:90", "aspectMode": "cover", "animated": True }, { "contents": [ { "type": "text", "text": "💠", "size": "xxs", "color": "#FFD700", "align": "center" } ], "type": "box", "layout": "vertical" }, { "contents": [ { "type": "text", "text": "💠", "size": "xxs", "color": "#FFD700", "align": "center" } ], "type": "box", "layout": "vertical" }, { "contents": [ { "type": "text", "text": "⭐", "size": "xxs", "color": "#FFD700", "align": "center" } ], "type": "box", "layout": "vertical" } ], "type": "box", "layout": "vertical", "borderWidth": "normal", "width": "20px", "height": "56px", "alignItems": "center", "justifyContent": "center" } ], "type": "box", "layout": "vertical", "flex": 1, "borderWidth": "normal" }, { "contents": [ { "contents": [ { "type": "image", "url": "https://i.ibb.co/MCJvn4h/ezgif-com-gif-to-apng-2022-02-03-T105057-954.png", "size": "full", "position": "absolute", "aspectRatio": "40:40", "aspectMode": "cover", "animated": True }, { "contents": [ { "type": "image", "url": url, "size": "md", "position": "absolute", "offsetTop": "0px", "offsetBottom": "0px", "offsetStart": "0px", "offsetEnd": "0px", "aspectRatio": "1:1" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://i.ibb.co/wYBvT0H/ezgif-com-gif-to-apng-13.png", "size": "xxl", "animated": True } ] } ], "type": "box", "layout": "vertical", "alignItems": "center", "justifyContent": "center", "cornerRadius": "xs", "width": "95px", "height": "95px" } ], "type": "box", "layout": "vertical", "borderWidth": "normal", "width": "110px", "height": "110px", "alignItems": "center", "justifyContent": "center" },
   { "contents": [ { "type": "image", "url": "https://i.ibb.co/mhhTTSJ/ezgif-com-gif-to-apng-32.png", "position": "absolute", "size": "full", "aspectRatio": "160:25", "aspectMode": "cover", "animated": True }, { "type": "text", "text": name, "size": "xxs", "color": "#FFD700", "align": "center" } ], "type": "box", "layout": "vertical", "borderWidth": "normal" } ], "type": "box", "layout": "vertical", "flex": 6, "borderWidth": "2px" }, { "contents": [ { "contents": [ { "type": "text", "text": "🌺", "size": "xs", "color": "#FFD700", "align": "center" } ], "type": "box", "layout": "vertical" }, { "contents": [ { "type": "text", "text": "G", "weight": "bold", "size": "xs", "color": "#33FFCC", "align": "center" } ], "type": "box", "layout": "vertical" }, { "contents": [ { "type": "text", "text": "R", "size": "xs", "weight": "bold", "color": "#33FFCC", "align": "center" } ], "type": "box", "layout": "vertical" }, { "contents": [ { "type": "text", "text": "O", "weight": "bold", "size": "xs", "color": "#33FFCC", "align": "center" } ], "type": "box", "layout": "vertical" }, { "contents": [ { "type": "text", "text": "U", "size": "xs", "weight": "bold", "color": "#33FFCC", "align": "center" } ], "type": "box", "layout": "vertical" }, { "contents": [ { "type": "text", "text": "P", "weight": "bold", "size": "xs", "color": "#33FFCC", "align": "center" } ], "type": "box", "layout": "vertical" }, { "contents": [ { "type": "text", "text": "🌺", "size": "xs", "color": "#FFD700", "align": "center" } ], "type": "box", "layout": "vertical" } ], "type": "box", "layout": "vertical", "flex": 1, "borderWidth": "normal" } ], "type": "box", "layout": "horizontal", "borderWidth": "2px" }, { "contents": [ { "type": "image", "url": "https://i.ibb.co/59kmj6W/ezgif-com-gif-to-apng-2022-02-02-T234933-721.png", "size": "full", "aspectMode": "cover", "position": "absolute", "aspectRatio": "160:30", "animated": True }, { "type": "text", "text": "Selamat bergabung  friend 😃😃\nSmoga betah jangan baperan ya.🤗 ", "size": "xxs", "color": "#00FFFF", "align": "center", "wrap": True } ], "type": "box", "layout": "vertical", "borderWidth": "normal", "width": "160px", "height": "30px", "justifyContent": "center", "alignItems": "center", "borderColor": "#FF0000cc" }, { "contents": [ { "contents": [ { "url": "https://i.ibb.co/VjBvDF9/ezgif-com-gif-to-apng-29.png", "size": "full", "type": "image", "animated": True, "backgroundColor": "#000000cc" } ], "type": "box", "layout": "vertical", "borderColor": "#00FF00", "cornerRadius": "xl", "borderWidth": "light" }, { "contents": [ { "contents": [ { "contents": [ { "type": "text", "text": "©VTEAM-OFFICIAL", "size": "xxs", "align": "center", "color": "#AFEEEE", "action": { "type": "uri", "uri": "https://line.me/ti/p/~mikhaell14" } } ], "type": "box", "layout": "vertical", "flex": 4, "borderWidth": "light", "borderColor": "#40E0D0cc", "cornerRadius": "xxl", "justifyContent": "center", "alignItems": "center" } ], "type": "box", "layout": "horizontal", "alignItems": "center", "justifyContent": "center" } ], "type": "box", "layout": "vertical", "flex": 7, "justifyContent": "center", "alignItems": "center" }, { "contents": [ { "url": "https://i.ibb.co/VjBvDF9/ezgif-com-gif-to-apng-29.png", "size": "full", "type": "image", "animated": True, "backgroundColor": "#000000cc" } ], "type": "box", "layout": "vertical", "borderColor": "#00FF00", "cornerRadius": "xl", "borderWidth": "light" } ], "type": "box", "layout": "horizontal", "borderWidth": "medium", "borderColor": "#0000FFcc" } ], "type": "box", "layout": "vertical" } ], "type": "box", "spacing": "md", "layout": "vertical" } ], "paddingAll": "0px", "backgroundColor": "#000000", "cornerRadius": "md", "justifyContent": "center", "borderColor": "#00FFFFcc", "alignItems": "center" }, "styles": { "body": { "backgroundColor": "#000000" } } } ] }
    message = FlexSendMessage(alt_text="©VTEAM-OFFICIAL", contents=data)
    Xeberlhyn.reply_message(to, message)

@handler.add(JoinEvent)
def handle_join(event):
    to = event.reply_token
    room = event.source.group_id
    G = Xeberlhyn.get_group_summary(room)
    url = G.picture_url
    name = G.group_name
    data = { "type": "carousel", "contents": [ { "type": "bubble", "size": "micro", "body": { "borderWidth": "medium", "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://i.ibb.co/XJgtjWQ/ezgif-com-gif-to-apng-2022-02-03-T111625-179.png", "position": "absolute", "aspectMode": "cover", "offsetTop": "0px", "offsetBottom": "0px", "offsetStart": "0px", "offsetEnd": "0px", "size": "full", "aspectRatio": "2:3", "backgroundColor": "#8A2BE2cc", "animated": True }, { "contents": [ { "contents": [ { "contents": [ { "contents": [ { "type": "text", "text": "🌼 AUTO JOIN MESSAGE 🌼", "size": "xxs", "color": "#F5F5DC", "weight": "bold", "align": "center", "gravity": "center" }, { "type": "separator", "color": "#FF1493" }, { "type": "separator", "color": "#FF1493" }, { "type": "separator", "color": "#FF1493" } ], "type": "box", "layout": "vertical", "backgroundColor": "#40E0D0cc" } ], "type": "box", "layout": "horizontal" }, { "contents": [ { "contents": [ { "contents": [ { "type": "image", "url": "https://i.ibb.co/JkQx1vY/ezgif-com-gif-to-apng-2022-02-03-T103541-832.png", "position": "absolute", "size": "full", "aspectRatio": "30:90", "aspectMode": "cover", "animated": True }, { "contents": [ { "type": "text", "text": "🌺", "size": "xxs", "color": "#FFD700", "align": "center" } ], "type": "box", "layout": "vertical" }, { "contents": [ { "type": "text", "text": "💠", "size": "xxs", "color": "#FFD700", "align": "center" } ], "type": "box", "layout": "vertical" }, { "contents": [ { "type": "text", "text": "🌺", "size": "xxs", "color": "#FFD700", "align": "center" } ], "type": "box", "layout": "vertical" } ], "type": "box", "layout": "vertical", "borderWidth": "normal", "width": "20px", "height": "56px", "alignItems": "center", "justifyContent": "center" },
   { "contents": [ { "contents": [ { "type": "text", "text": "⏩", "size": "xxs", "color": "#FFD700", "align": "center", "gravity": "center" } ], "type": "box", "layout": "vertical" } ], "type": "box", "layout": "vertical", "borderWidth": "normal" } ], "type": "box", "layout": "vertical", "flex": 1, "borderWidth": "normal" }, { "contents": [ { "contents": [ { "contents": [ { "type": "image", "url": "https://i.ibb.co/MCJvn4h/ezgif-com-gif-to-apng-2022-02-03-T105057-954.png", "size": "full", "position": "absolute", "aspectRatio": "20:20", "aspectMode": "cover", "animated": True }, { "contents": [ { "type": "image", "url": url, "size": "md", "position": "absolute", "offsetTop": "0px", "offsetBottom": "0px", "offsetStart": "0px", "offsetEnd": "0px", "aspectRatio": "1:1" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://i.ibb.co/wYBvT0H/ezgif-com-gif-to-apng-13.png", "size": "xxl", "animated": True } ] } ], "type": "box", "layout": "vertical", "alignItems": "center", "justifyContent": "center", "cornerRadius": "xs", "width": "47px", "height": "47px" } ], "type": "box", "layout": "vertical", "borderWidth": "normal", "width": "54px", "height": "54px", "alignItems": "center", "justifyContent": "center" }, { "contents": [ { "type": "image", "url": "https://i.ibb.co/JkQx1vY/ezgif-com-gif-to-apng-2022-02-03-T103541-832.png", "position": "absolute", "size": "full", "aspectRatio": "30:90", "aspectMode": "cover", "animated": True }, { "contents": [ { "type": "text", "text": "🌺", "size": "xxs", "color": "#FFD700", "align": "center" } ], "type": "box", "layout": "vertical" }, { "contents": [ { "type": "text", "text": "💠", "size": "xxs", "color": "#FFD700", "align": "center" } ], "type": "box", "layout": "vertical" }, { "contents": [ { "type": "text", "text": "🌺", "size": "xxs", "color": "#FFD700", "align": "center" } ], "type": "box", "layout": "vertical" } ], "type": "box", "layout": "vertical", "borderWidth": "normal", "width": "20px", "height": "53px", "alignItems": "center", "justifyContent": "center" }, { "contents": [ { "type": "image", "url": "https://i.ibb.co/VjBvDF9/ezgif-com-gif-to-apng-29.png", "size": "xxs", "animated": True, "aspectRatio": "1:1" } ], "type": "box", "layout": "vertical", "borderWidth": "normal" } ], "type": "box", "layout": "horizontal", "borderWidth": "normal", "spacing": "sm" }, { "contents": [ { "type": "image", "url": "https://i.ibb.co/NS474sY/ezgif-com-resize-5.png", "position": "absolute", "size": "full", "aspectRatio": "150:22", "aspectMode": "cover", "animated": True }, { "contents": [ { "type": "text", "text": name, "size": "xxs", "color": "#FFD700", "align": "center" } ], "type": "box", "layout": "vertical", "borderWidth": "normal", "width": "123px", "height": "20px", "alignItems": "center" } ], "type": "box", "layout": "vertical", "borderWidth": "normal", "width": "130px", "height": "23px" } ], "type": "box", "layout": "vertical", "flex": 6, "borderWidth": "2px" } ], "type": "box", "layout": "horizontal" }, { "contents": [ { "type": "image", "url": "https://i.ibb.co/59kmj6W/ezgif-com-gif-to-apng-2022-02-02-T234933-721.png", "size": "full", "aspectMode": "cover", "position": "absolute", "aspectRatio": "160:30", "animated": True }, { "type": "text", "text": "Terimakasih telah diinvite\nketik 'Menu' untuk fiture layanan.", "size": "xxs", "color": "#00FFFF", "align": "center", "wrap": True } ], "type": "box", "layout": "vertical", "borderWidth": "normal", "width": "160px", "height": "30px", "justifyContent": "center", "alignItems": "center" }, { "type": "separator", "color": "#FF1493" }, { "type": "separator", "color": "#FF1493" }, { "type": "separator", "color": "#FF1493" }, { "contents": [ { "contents": [ { "url": "https://i.ibb.co/VjBvDF9/ezgif-com-gif-to-apng-29.png", "size": "full", "type": "image", "animated": True, "backgroundColor": "#000000cc" } ], "type": "box", "layout": "vertical", "borderColor": "#8B4513", "cornerRadius": "xl", "borderWidth": "light" }, { "contents": [ { "contents": [ { "contents": [ { "type": "text", "text": "©VTEAM-OFFICIAL", "size": "xxs", "align": "center", "color": "#000000cc", "action": { "type": "uri", "uri": "https://line.me/ti/p/~mikhaell14" } } ], "type": "box", "layout": "vertical", "flex": 4, "borderWidth": "light", "borderColor": "#8B4513cc", "cornerRadius": "xxl", "justifyContent": "center", "alignItems": "center" } ], "type": "box", "layout": "horizontal", "alignItems": "center", "justifyContent": "center" } ], "type": "box", "layout": "vertical", "flex": 7, "justifyContent": "center", "alignItems": "center" }, { "contents": [ { "url": "https://i.ibb.co/VjBvDF9/ezgif-com-gif-to-apng-29.png", "size": "full", "type": "image", "animated": True, "backgroundColor": "#000000cc" } ], "type": "box", "layout": "vertical", "borderColor": "#8B4513", "cornerRadius": "xl", "borderWidth": "light" } ], "type": "box", "layout": "horizontal", "borderWidth": "medium", "backgroundColor": "#40E0D0cc" } ], "type": "box", "layout": "vertical" } ], "type": "box", "spacing": "xs", "layout": "vertical" } ], "paddingAll": "0px", "cornerRadius": "md", "justifyContent": "center", "borderColor": "#40E0D0cc", "alignItems": "center" }, "styles": { "body": { "backgroundColor": "#000000" } } } ] }
    Xeberlhyn.reply_message(to, FlexSendMessage(alt_text="©VTEAM-OFFICIAL", contents=data))

@handler.add(FollowEvent)
def handle_follow(event):
    to = event.reply_token
    pelaku = event.source.user_id
    G = Xeberlhyn.get_profile(pelaku)
    url = G.picture_url
    name = G.display_name
    data = { "type": "carousel", "contents": [ { "type": "bubble", "size": "micro", "body": { "borderWidth": "medium", "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://i.ibb.co/XJgtjWQ/ezgif-com-gif-to-apng-2022-02-03-T111625-179.png", "position": "absolute", "aspectMode": "cover", "offsetTop": "0px", "offsetBottom": "0px", "offsetStart": "0px", "offsetEnd": "0px", "size": "full", "aspectRatio": "2:3", "backgroundColor": "#8A2BE2cc", "animated": True }, { "contents": [ { "contents": [ { "contents": [ { "contents": [ { "type": "text", "text": "🌼 AUTO ADD MESSAGE 🌼", "size": "xxs", "color": "#F5F5DC", "weight": "bold", "align": "center", "gravity": "center" }, { "type": "separator", "color": "#FF1493" }, { "type": "separator", "color": "#FF1493" }, { "type": "separator", "color": "#FF1493" } ], "type": "box", "layout": "vertical", "backgroundColor": "#40E0D0cc" } ], "type": "box", "layout": "horizontal" }, { "contents": [ { "contents": [ { "contents": [ { "type": "image", "url": "https://i.ibb.co/JkQx1vY/ezgif-com-gif-to-apng-2022-02-03-T103541-832.png", "position": "absolute", "size": "full", "aspectRatio": "30:90", "aspectMode": "cover", "animated": True }, { "contents": [ { "type": "text", "text": "🌺", "size": "xxs", "color": "#FFD700", "align": "center" } ], "type": "box", "layout": "vertical" }, { "contents": [ { "type": "text", "text": "💠", "size": "xxs", "color": "#FFD700", "align": "center" } ], "type": "box", "layout": "vertical" }, { "contents": [ { "type": "text", "text": "🌺", "size": "xxs", "color": "#FFD700", "align": "center" } ], "type": "box", "layout": "vertical" } ], "type": "box", "layout": "vertical", "borderWidth": "normal", "width": "20px", "height": "56px", "alignItems": "center", "justifyContent": "center" },
    { "contents": [ { "contents": [ { "type": "text", "text": "⏩", "size": "xxs", "color": "#FFD700", "align": "center", "gravity": "center" } ], "type": "box", "layout": "vertical" } ], "type": "box", "layout": "vertical", "borderWidth": "normal" } ], "type": "box", "layout": "vertical", "flex": 1, "borderWidth": "normal" }, { "contents": [ { "contents": [ { "contents": [ { "type": "image", "url": "https://i.ibb.co/MCJvn4h/ezgif-com-gif-to-apng-2022-02-03-T105057-954.png", "size": "full", "position": "absolute", "aspectRatio": "20:20", "aspectMode": "cover", "animated": True }, { "contents": [ { "type": "image", "url": url, "size": "md", "position": "absolute", "offsetTop": "0px", "offsetBottom": "0px", "offsetStart": "0px", "offsetEnd": "0px", "aspectRatio": "1:1" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "https://i.ibb.co/wYBvT0H/ezgif-com-gif-to-apng-13.png", "size": "xxl", "animated": True } ] } ], "type": "box", "layout": "vertical", "alignItems": "center", "justifyContent": "center", "cornerRadius": "xs", "width": "47px", "height": "47px" } ], "type": "box", "layout": "vertical", "borderWidth": "normal", "width": "54px", "height": "54px", "alignItems": "center", "justifyContent": "center" }, { "contents": [ { "type": "image", "url": "https://i.ibb.co/JkQx1vY/ezgif-com-gif-to-apng-2022-02-03-T103541-832.png", "position": "absolute", "size": "full", "aspectRatio": "30:90", "aspectMode": "cover", "animated": True }, { "contents": [ { "type": "text", "text": "🌺", "size": "xxs", "color": "#FFD700", "align": "center" } ], "type": "box", "layout": "vertical" }, { "contents": [ { "type": "text", "text": "💠", "size": "xxs", "color": "#FFD700", "align": "center" } ], "type": "box", "layout": "vertical" }, { "contents": [ { "type": "text", "text": "🌺", "size": "xxs", "color": "#FFD700", "align": "center" } ], "type": "box", "layout": "vertical" } ], "type": "box", "layout": "vertical", "borderWidth": "normal", "width": "20px", "height": "53px", "alignItems": "center", "justifyContent": "center" }, { "contents": [ { "type": "image", "url": "https://i.ibb.co/VjBvDF9/ezgif-com-gif-to-apng-29.png", "size": "xxs", "animated": True, "aspectRatio": "1:1" } ], "type": "box", "layout": "vertical", "borderWidth": "normal" } ], "type": "box", "layout": "horizontal", "borderWidth": "normal", "spacing": "sm" }, { "contents": [ { "type": "image", "url": "https://i.ibb.co/NS474sY/ezgif-com-resize-5.png", "position": "absolute", "size": "full", "aspectRatio": "150:22", "aspectMode": "cover", "animated": True }, { "contents": [ { "type": "text", "text": name, "size": "xxs", "color": "#FFD700", "align": "center" } ], "type": "box", "layout": "vertical", "borderWidth": "normal", "width": "123px", "height": "20px", "alignItems": "center" } ], "type": "box", "layout": "vertical", "borderWidth": "normal", "width": "130px", "height": "23px" } ], "type": "box", "layout": "vertical", "flex": 6, "borderWidth": "2px" } ], "type": "box", "layout": "horizontal" }, { "contents": [ { "type": "image", "url": "https://i.ibb.co/59kmj6W/ezgif-com-gif-to-apng-2022-02-02-T234933-721.png", "size": "full", "aspectMode": "cover", "position": "absolute", "aspectRatio": "160:30", "animated": True }, { "type": "text", "text": "Hello dear, saya udah add balik,\nApa yang bisa saya bantu.?", "size": "xxs", "color": "#00FFFF", "align": "center", "wrap": True } ], "type": "box", "layout": "vertical", "borderWidth": "normal", "width": "160px", "height": "30px", "justifyContent": "center", "alignItems": "center" }, { "type": "separator", "color": "#FF1493" }, { "type": "separator", "color": "#FF1493" }, { "type": "separator", "color": "#FF1493" }, { "contents": [ { "contents": [ { "url": "https://i.ibb.co/VjBvDF9/ezgif-com-gif-to-apng-29.png", "size": "full", "type": "image", "animated": True, "backgroundColor": "#000000cc" } ], "type": "box", "layout": "vertical", "borderColor": "#8B4513", "cornerRadius": "xl", "borderWidth": "light" }, { "contents": [ { "contents": [ { "contents": [ { "type": "text", "text": "©VTEAM-OFFICIAL", "size": "xxs", "align": "center", "color": "#000000cc", "action": { "type": "uri", "uri": "https://line.me/ti/p/~mikhaell14" } } ], "type": "box", "layout": "vertical", "flex": 4, "borderWidth": "light", "borderColor": "#8B4513cc", "cornerRadius": "xxl", "justifyContent": "center", "alignItems": "center" } ], "type": "box", "layout": "horizontal", "alignItems": "center", "justifyContent": "center" } ], "type": "box", "layout": "vertical", "flex": 7, "justifyContent": "center", "alignItems": "center" }, { "contents": [ { "url": "https://i.ibb.co/VjBvDF9/ezgif-com-gif-to-apng-29.png", "size": "full", "type": "image", "animated": True, "backgroundColor": "#000000cc" } ], "type": "box", "layout": "vertical", "borderColor": "#8B4513", "cornerRadius": "xl", "borderWidth": "light" } ], "type": "box", "layout": "horizontal", "borderWidth": "medium", "backgroundColor": "#40E0D0cc" } ], "type": "box", "layout": "vertical" } ], "type": "box", "spacing": "xs", "layout": "vertical" } ], "paddingAll": "0px", "cornerRadius": "md", "justifyContent": "center", "borderColor": "#40E0D0cc", "alignItems": "center" }, "styles": { "body": { "backgroundColor": "#000000" } } } ] }
    Xeberlhyn.reply_message(to, FlexSendMessage(alt_text="©VTEAM-OFFICIAL", contents=data))

#____________batas dev__________________
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    tks = str(event.message.text)
    VinsenT = tks.lower()
    sender = event.source.user_id
    msg_id = event.message.id
    to = event.reply_token
    room = event.source.group_id
    if VinsenT == 'mid':
        x = datetime.datetime.now()
        profile = Xeberlhyn.get_profile(sender)
        url = profile.picture_url
        a_ = "「 𝗕𝗢𝗧 𝗜𝗡𝗙𝗢𝗥𝗠𝗔𝗧𝗜𝗢𝗡」\n"
        a_ += "\n⌬ 𝗡𝗮𝗺𝗲 : "+str(profile.display_name)
        a_ += "\n⌬ {}".format(str(sender))
        a_ += "\n\n𝐕 𝐓 ΞΛ𝐌 • 𝐒𝐘𝐒𝐓𝐄𝐌"
        data =  { "type": "carousel", "contents": [{ "type": "bubble", "size": "deca", "body": { "type": "box", "layout": "vertical", "contents": [ { "type": "box", "layout": "horizontal", "contents": [ { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": "{}".format(url), "aspectMode": "cover", "size": "full" } ], "cornerRadius": "100px", "width": "20px", "height": "20px" }, { "type": "box", "layout": "horizontal", "contents": [ { "type": "text", "contents": [], "text": "𝐕𝐓𝐄𝐀𝐌 𝐎𝐅𝐅𝐈𝐂𝐈𝐀𝐋 | 𝙸 𝚊𝚖 𝚛𝚘𝚋𝚘𝚝 𝚕𝚒𝚗𝚎", "size": "10px", "weight": "bold" } ], "justifyContent": "center", "alignItems": "center" } ], "spacing": "md" }, { "type": "separator", "margin": "xs", "color": "#708090" }, { "type": "box", "layout": "horizontal", "contents": [ { "type": "text", "contents": [ { "type": "span", "text": "Jam {}".format(str(x.strftime("%I:%M:%S %p"))), "size": "8px", "weight": "bold", "color": "#778899cc" } ] }, { "type": "text", "contents": [ { "type": "span", "text": "{}".format(str(x.strftime("%A, %d %b %Y"))), "size": "8px", "weight": "bold", "color": "#778899cc" } ], "align": "end" } ] }, { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "{}".format(str(a_)), "wrap": True, "size": "8px" } ] }, { "type": "separator", "color": "#708090" }, { "type": "box", "layout": "horizontal", "contents": [ { "type": "box", "layout": "vertical", "contents": [ { "type": "text", "text": "𝐏𝐥𝐞𝐚𝐬𝐞 𝐜𝐥𝐢𝐜𝐤 𝐭𝐨 𝐎𝐰𝐧𝐞𝐫", "size": "10px", "weight": "bold", "decoration": "underline", "action": { "type": "uri", "uri": "line.me/ti/p/~xeberlhyn23" }, "color": "#0000FFCC" } ], "justifyContent": "center", "alignItems": "center" }, { "type": "box", "layout": "vertical", "contents": [ { "type": "image", "url": Xeberlhyn.get_profile("Uab4a2365a6a7a901cb09984f618d36d8").picture_url, "size": "full", "aspectMode": "cover" } ], "width": "20px", "height": "20px", "borderWidth": "normal", "cornerRadius": "xxl" } ], "margin": "sm" } ], "paddingAll": "3px" }]}
        Xeberlhyn.reply_message(to, FlexSendMessage(alt_text="©VTEAM-OFFICIAL", contents=data))

#______________________________________________________________________
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except LineBotApiError as e:
        print("Got exception from LINE Messaging API: %s\n" % e.message)
        for m in e.error.details:
            print("  %s: %s" % (m.property, m.message))
        print("\n")
    except InvalidSignatureError:
        abort(400)
    return 'OK'
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
