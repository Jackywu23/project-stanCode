"""
File: my_drawing.py
Name: Jacky Wu
----------------------
Using object to make a drawing
"""

from campy.graphics.gobjects import GOval, GPolygon
from campy.graphics.gwindow import GWindow


def main():
    """
    Title: Mirror Wheel Eye

    The idea comes from classic Japanese comic, Naruto. The Mirror Wheel Eye
    can control others and make special actions.
    """
    window = GWindow(width=610, height=621, title="Mirror Wheel Eye")
    # outer contour
    d1 = 291
    body = GOval(d1*2, d1*2, x=window.width/2 - d1, y=window.height/2 - d1)
    body.filled = True
    body.fill_color = "black"
    window.add(body)

    # inner body
    d2 = 264
    inner_body = GOval(d2*2, d2*2, x=window.width / 2 - d2, y=window.height / 2 - d2)
    inner_body.filled = True
    inner_body.fill_color = "darkred"
    window.add(inner_body)

    # Second layer dark body
    d3 = 208
    inner_body2 = GOval(d3 * 2, d3 * 2, x=window.width / 2 - d3, y=window.height / 2 - d3)
    inner_body2.filled = True
    inner_body2.fill_color = "black"
    window.add(inner_body2)

    # Second layer red body
    d4 = 186
    inner_body3 = GOval(d4 * 2, d4 * 2, x=window.width / 2 - d4, y=window.height / 2 - d4)
    inner_body3.filled = True
    inner_body3.fill_color = "darkred"
    window.add(inner_body3)

    # Eyes contour1
    eyes = GPolygon()
    eyes.add_vertex((306, 299))  # 原點
    eyes.add_vertex((240, 354))  # 起始點
    eyes.add_vertex((172, 294))
    eyes.add_vertex((128, 251))
    eyes.add_vertex((90, 201))
    eyes.add_vertex((71, 172))
    eyes.add_vertex((83, 152))
    eyes.add_vertex((121, 156))
    eyes.add_vertex((171, 166))
    eyes.add_vertex((213, 183))
    eyes.add_vertex((300, 216))  # 最後一點
    eyes.filled = True
    eyes.fill_color = "black"
    window.add(eyes)

    # Eyes contour1_add
    eyes_add = GPolygon()
    eyes_add.add_vertex((74, 171))
    eyes_add.add_vertex((93, 149))
    eyes_add.add_vertex((107, 137))
    eyes_add.add_vertex((122, 129))
    eyes_add.add_vertex((136, 119))
    eyes_add.add_vertex((154, 112))
    eyes_add.add_vertex((169, 105))
    eyes_add.add_vertex((186, 99))
    eyes_add.add_vertex((199, 94))
    eyes_add.add_vertex((213, 90))
    eyes_add.add_vertex((226, 89))
    eyes_add.add_vertex((240, 87))
    eyes_add.add_vertex((254, 86))
    eyes_add.add_vertex((268, 88))
    eyes_add.add_vertex((282, 88))
    eyes_add.add_vertex((297, 90))
    eyes_add.add_vertex((312, 93))
    eyes_add.add_vertex((323, 95))
    eyes_add.add_vertex((347, 102))
    eyes_add.add_vertex((357, 108))
    eyes_add.add_vertex((369, 114))
    eyes_add.add_vertex((344, 115))
    eyes_add.add_vertex((321, 111))
    eyes_add.add_vertex((306, 109))
    eyes_add.add_vertex((287, 111))
    eyes_add.add_vertex((275, 110))
    eyes_add.add_vertex((256, 113))
    eyes_add.add_vertex((241, 116))
    eyes_add.add_vertex((226, 122))
    eyes_add.add_vertex((205, 134))
    eyes_add.add_vertex((190, 143))
    eyes_add.add_vertex((180, 152))
    eyes_add.add_vertex((170, 162))
    eyes_add.add_vertex((153, 172))
    eyes_add.filled = True
    eyes_add.fill_color = "black"
    window.add(eyes_add)

    # Eyes contour2
    eyes1 = GPolygon()
    eyes1.add_vertex((306, 299))  # 原點
    eyes1.add_vertex((240, 354))  # 起始點
    eyes1.add_vertex((260, 487))
    eyes1.add_vertex((268, 516))
    eyes1.add_vertex((307, 578))
    eyes1.add_vertex((334, 517))
    eyes1.add_vertex((357, 481))
    eyes1.add_vertex((387, 335))
    eyes1.filled = True
    eyes1.fill_color = "black"
    window.add(eyes1)

    # Eyes contour2_add
    eyes1_add = GPolygon()
    eyes1_add.add_vertex((260, 487))
    eyes1_add.add_vertex((268, 516))
    eyes1_add.add_vertex((307, 578))
    eyes1_add.add_vertex((294, 578))
    eyes1_add.add_vertex((283, 571))
    eyes1_add.add_vertex((269, 565))
    eyes1_add.add_vertex((258, 559))
    eyes1_add.add_vertex((248, 552))
    eyes1_add.add_vertex((236, 545))
    eyes1_add.add_vertex((225, 539))
    eyes1_add.add_vertex((215, 532))
    eyes1_add.add_vertex((203, 525))
    eyes1_add.add_vertex((197, 517))
    eyes1_add.add_vertex((189, 509))
    eyes1_add.add_vertex((181, 501))
    eyes1_add.add_vertex((174, 493))
    eyes1_add.add_vertex((169, 486))
    eyes1_add.add_vertex((163, 478))
    eyes1_add.add_vertex((156, 469))
    eyes1_add.add_vertex((151, 461))
    eyes1_add.add_vertex((146, 451))
    eyes1_add.add_vertex((141, 443))
    eyes1_add.add_vertex((137, 434))
    eyes1_add.add_vertex((132, 422))
    eyes1_add.add_vertex((129, 414))
    eyes1_add.add_vertex((127, 407))
    eyes1_add.add_vertex((124, 396))
    eyes1_add.add_vertex((121, 388))
    eyes1_add.add_vertex((119, 380))
    eyes1_add.add_vertex((117, 370))
    eyes1_add.add_vertex((116, 360))
    eyes1_add.add_vertex((115, 350))
    eyes1_add.add_vertex((114, 341))
    eyes1_add.add_vertex((124, 359))
    eyes1_add.add_vertex((130, 375))
    eyes1_add.add_vertex((136, 390))
    eyes1_add.add_vertex((141, 403))
    eyes1_add.add_vertex((146, 416))
    eyes1_add.add_vertex((158, 434))
    eyes1_add.add_vertex((170, 447))
    eyes1_add.add_vertex((177, 455))
    eyes1_add.add_vertex((191, 466))
    eyes1_add.add_vertex((206, 477))
    eyes1_add.add_vertex((223, 491))
    eyes1_add.filled = True
    eyes1_add.fill_color = "black"
    window.add(eyes1_add)

    # Eyes contour3
    eyes2 = GPolygon()
    eyes2.add_vertex((306, 299))  # 原點
    eyes2.add_vertex((387, 335))  # 起始點
    eyes2.add_vertex((492, 250))
    eyes2.add_vertex((523, 222))
    eyes2.add_vertex((547, 196))
    eyes2.add_vertex((545, 163))
    eyes2.add_vertex((475, 171))
    eyes2.add_vertex((441, 170))
    eyes2.add_vertex((300, 216))
    eyes2.filled = True
    eyes2.fill_color = "black"
    window.add(eyes2)

    # Eyes contour3_add
    eyes2_add = GPolygon()
    eyes2_add.add_vertex((492, 250))
    eyes2_add.add_vertex((523, 222))
    eyes2_add.add_vertex((547, 196))
    eyes2_add.add_vertex((548, 224))
    eyes2_add.add_vertex((549, 250))
    eyes2_add.add_vertex((548, 261))
    eyes2_add.add_vertex((547, 271))
    eyes2_add.add_vertex((544, 279))
    eyes2_add.add_vertex((544, 288))
    eyes2_add.add_vertex((542, 296))
    eyes2_add.add_vertex((540, 305))
    eyes2_add.add_vertex((537, 317))
    eyes2_add.add_vertex((532, 326))
    eyes2_add.add_vertex((529, 336))
    eyes2_add.add_vertex((524, 347))
    eyes2_add.add_vertex((519, 361))
    eyes2_add.add_vertex((512, 370))
    eyes2_add.add_vertex((506, 381))
    eyes2_add.add_vertex((499, 390))
    eyes2_add.add_vertex((491, 397))
    eyes2_add.add_vertex((484, 404))
    eyes2_add.add_vertex((476, 409))
    eyes2_add.add_vertex((481, 397))
    eyes2_add.add_vertex((486, 387))
    eyes2_add.add_vertex((492, 379))
    eyes2_add.add_vertex((494, 370))
    eyes2_add.add_vertex((499, 359))
    eyes2_add.add_vertex((505, 347))
    eyes2_add.add_vertex((509, 331))
    eyes2_add.add_vertex((507, 317))
    eyes2_add.add_vertex((509, 300))
    eyes2_add.add_vertex((508, 283))
    eyes2_add.add_vertex((507, 264))
    eyes2_add.filled = True
    eyes2_add.fill_color = "black"
    window.add(eyes2_add)

    # last layer red body
    d5 = 63
    inner_body4 = GOval(d5 * 2, d5 * 2, x=window.width / 2 - d5, y=window.height / 2 - d5)
    inner_body4.filled = True
    inner_body4.fill_color = "darkred"
    window.add(inner_body4)


if __name__ == '__main__':
    main()
