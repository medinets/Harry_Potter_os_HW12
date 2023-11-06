class Player:
    def __init__(self, name, video_link, duration):
        self.name = name
        self.video_link = video_link
        self.duration = duration
        self.playing = True
        self.quality = "HD"

    def play(self, video_link):
        return video_link == self.video_link
    def pause(self):
        self.playing = not(self.playing)
    def change_quality(self, quality):
        self.quality = quality