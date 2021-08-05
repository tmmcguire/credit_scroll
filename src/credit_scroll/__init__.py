import moviepy.editor as mpy
from moviepy.video.fx.scroll import scroll

WIDTH        = 1280
HEIGHT       = 720
DURATION     = 30
FPS          = 30
E_EDGE       = WIDTH * 0.1
W_EDGE       = WIDTH * 0.9
COLOR        = 'White'
FONT         = 'Noto-Sans-Bold'
FONTSIZE     = 34
STROKE_COLOR = 'black'
STROKE_WIDTH = 0.5

def toTextClip(txt, align='Center'):
    return mpy.TextClip(
        txt          = len(txt) == 0 and ' ' or txt,
        align        = align,
        font         = FONT,
        fontsize     = FONTSIZE,
        color        = COLOR,
        stroke_color = STROKE_COLOR,
        stroke_width = STROKE_WIDTH,
    )

def toClip(ln):
    if type(ln) is tuple:
        east   = toTextClip(ln[0], align='East')
        west   = toTextClip(ln[1], align='West')
        height = max(east.h, west.h)
        return mpy.CompositeVideoClip(
            [
                east.set_position((E_EDGE, 0)),
                west.set_position((W_EDGE - west.w, 0)),
            ],
            size = (1280, height)
        )
    else:
        return toTextClip(ln)

def makePos(length):
    def pos(t):
        time = t / DURATION
        return ('center', HEIGHT - (length * time))
    return pos

def writeCredits(credits, file):
    clips = [toClip(ln) for ln in credits]
    maxh = max([clip.h for clip in clips])
    clips = [clip.set_position(('center', maxh * count)) for (count, clip) in enumerate(clips) ]
    clip = mpy.CompositeVideoClip(
        clips,
        size=(WIDTH, sum([clip.h for clip in clips]))
    ).set_duration(DURATION).set_fps(FPS)
    length = HEIGHT + clip.h
    clip = mpy.CompositeVideoClip(
        [clip.set_position(makePos(length))],
        size=(WIDTH, HEIGHT)
    ).set_duration(DURATION).set_fps(FPS)
    clip.write_videofile(file)
