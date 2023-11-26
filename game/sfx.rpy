init:
    image particleFog = SnowBlossom("fog-particle.png", count=80, border=1000, xspeed=(15, 70), yspeed=(-5, 7), start=5, fast=True, horizontal=True)

    image particleFog2 = SnowBlossom("fog-particle.png", count=80, border=600, xspeed=-50, yspeed=0, start=-5, fast=True, horizontal=True)

    image tiledFog = im.Tile(im.Scale("fog.png", 1600, 600), size=(2400, 800))
