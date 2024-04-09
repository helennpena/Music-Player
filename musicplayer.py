import vlc
from mutagen.mp3 import MP3


songs_url = [
  "By The Way.mp3",
  "dontmatter.mp3",
  "havana.mp3",
  "uptown.mp3",
  "someone.mp3",
]

songs_title = [
  "By The Way", 
  "Don't Matter",
  "Havana",
  "Uptown Funk",
  "Someone Like You",
]

songs_artist = [
  "Red Hot Chili Peppers", 
  "Akon",
  "Camila Cabello",
  "Bruno Mars",
  "Adele",
]


vlc_instance = vlc.Instance('--no-xlib')
player = vlc_instance.media_player_new()
current_index = None
track_duration = 0
media = None

def play(e):
  global current_index
  global media
  global track_duration

  current_index = e
  audiopath = f"appflet/project/assets/{songs_url[current_index]}"
  media = vlc_instance.media_new(audiopath)
  player.set_media(media)
  player.play()
  track_duration = round(MP3(audiopath).info.length)
  minutes = round(track_duration // 60)
  seconds = round(track_duration % 60)

  print("Now Playing")
  print("------------------------")
  print(f"♪ {songs_title[current_index]} | {songs_artist[current_index]} | {minutes}:{seconds}")
  menu()

def playPause():
  global current_index
  global media
  if player.is_playing():
    player.pause()
  else:
    if media == None:
      play(0)
    else:
      player.play()
  menu()

def mute():
  global current_index
  global player

  is_muted = player.audio_get_mute()
    
  if is_muted:
    player.audio_set_mute(False)
  else:
    player.audio_set_mute(True)
  menu()

def menu():
  print("Audio Player Menu")
  print("------------------------")
  for i, music in enumerate(songs_title):
    music = songs_title[i]
    print(f"{music}")

  correctOption = False
  
  while correctOption == False:
    print("------------------------")
    print("1. Play track 1")
    print("2. Play track 2")
    print("3. Play track 3")
    print("4. Play track 4")
    print("5. Play track 5")
    print("6. Pause / Resume")
    print("7. Mute / Unmute")
    print("8. Exit")
    try:
      userinput = int(input("Select you desired option:\n"))
    except:
      print("incorrect input")
    if userinput >=1 and userinput <= 8:
      correctOption = True
      if userinput >=1 and userinput <= 5:
        play(userinput-1)
      elif userinput == 6:
        playPause()
      elif userinput == 7:
        mute()
      elif userinput == 8:
        return False

menu()
