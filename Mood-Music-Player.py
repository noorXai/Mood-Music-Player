import webbrowser  

# 🎵 Mood based music player (8 moods)
mood = input("How are you feeling today? (happy/sad/angry/lazy/romantic/focused/nostalgic/gangster): ").lower()  

if mood == "happy":  
    webbrowser.open("https://www.youtube.com/watch?v=w5tWYmIOWGk")  # On top of the world
elif mood == "sad":  
    webbrowser.open("https://www.youtube.com/watch?v=RBumgq5yVrA")  # Let her go
elif mood == "angry":  
    webbrowser.open("https://www.youtube.com/watch?v=PsO6ZnUZI0g")  # Stronger
elif mood == "lazy":  
    webbrowser.open("https://www.youtube.com/watch?v=ApXoWvfEYVU")  # Sunflower
elif mood == "romantic":  
    webbrowser.open("https://www.youtube.com/watch?v=Pkh8UtuejGw")  # Señorita
elif mood == "focused":  
    webbrowser.open("https://www.youtube.com/watch?v=nfs8NYg7yQM")  # Attention
elif mood == "nostalgic":  
    webbrowser.open("https://www.youtube.com/watch?v=3AtDnEC4zak")  # We Don’t Talk Anymore
elif mood == "gangster":  
    webbrowser.open("https://www.youtube.com/watch?v=_Yhyp-_hX2s")  # Lose Yourself
else:  
    print("😶 Unknown mood detected. Let's just chill...")  
