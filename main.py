import music_player
# Create a new instance of the MusicPlayer class
player = music_player.MusicPlayer("music")

# Define a dictionary of commands and their corresponding methods
commands = {
    "play": player.play_song,
    "p": player.play_song,
    "stop": player.stop_song,
    "s": player.stop_song,
    "pause": player.pause_song,
    "new": player.play_new_song, 
    "n": player.play_new_song,    
    "queue": player.queue_song,
    "q": player.queue_song,
    "volume": player.set_volume,
    "v": player.set_volume,
    "help": player.help,
    "exit": player.exit
}

# Loop to read commands from the user
while True:
    command = input("Enter a command: ")

  
    
    command = command.split(".")
    
    if command[0] in commands:
        if len(command) == 2:
            commands[command[0]](command[1])
        elif len(command) == 1:
            commands[command[0]]()
    else:
        print("\nInvalid command. Please try again.\nUse the 'help' command to view a list of commands.\n")