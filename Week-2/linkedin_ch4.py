# Following along with the linkedin course: Python for Non-Programmers by Nick Walter.
# I have a strong background in Python, so this is a quick refresher for me.


# <---- 4: Project 2 Lyric Analyzer ---->

# 4.1
lyrics = "I wanna be your endgame I wanna be your first string I wanna be your A-Team I wanna be your endgame, endgame"
print(lyrics)
print(len(lyrics))
print(len(lyrics.split()))


# 4.2
word_count = {}

for word in lyrics.lower().split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
        
print(word_count)