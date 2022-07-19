#就是播放一下母亲节的视频

import pyglet
def ShowVideo():
    vid_path = "源文件.mp4"

    window = pyglet.window.Window(width = 1920,height = 1080)

    player = pyglet.media.Player()
    source = pyglet.media.StreamingSource()
    MediaLoad = pyglet.media.load(vid_path)
    player.queue(MediaLoad)
    player.play()

    @window.event
    def on_draw():
        if player.source and player.source.video_format:
            player.get_texture().blit(0,0)


    pyglet.app.run()
