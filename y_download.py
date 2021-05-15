from pytube import YouTube

link = input("Link your video: ")
yt = YouTube(link)
videos = yt.streams.all()

video = list(enumerate(videos))

for i in video:
    print(i)
print()
print('''А сейчас вы должны выбрать нужный вам формат, 
просто введите цифру, например 1 это качевство 720р, и видео скачается туда же
где находится ваша дериктория''')
print()
dn_option = int(input("Введите опцию: "))
dn_video = videos[dn_option]
dn_video.download()
print()
print("Скачивание успешно заверешено")
print()