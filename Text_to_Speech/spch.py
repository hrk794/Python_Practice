#!/home/hrk/bin/python


# This script uses the gTTS library from Google to convert text from a file named tts.txt to speech and saves it as an mp3 file.


from gtts import gTTS


# Initialize a string variable
text = ""


# Open file to read it and, loop over the lines of the file to add them to the variable initialized earlier. 
with open("tts.txt", "r") as file:
	for line in file:
		text = text + line


# Convert the text in the variable to audio using the gTTS library and save it as an mp3 file.
speech = gTTS(text)
speech.save("audio.mp3")

