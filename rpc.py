from pypresence import Presence

CLIENT_ID = "1520322671278035065"

rpc = Presence(CLIENT_ID)


def connect():
    rpc.connect()


def update(start):

    rpc.update(

        details="Designing beautiful interfaces",

        state="Working on UI",

        large_image="figma",

        large_text="Figma",

        start=start,

    )
