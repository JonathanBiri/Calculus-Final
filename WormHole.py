from big_ol_pile_of_manim_imports import *

R = 1.4
ELL = 5
M = PI * R / 2.0
L = 2 * ELL + PI * R


def _half_bend(a, t):
    if t < 1e-6:
        return a, 0.0
    if a <= M:
        x = (R / t) * np.sin(t * a / R)
        y = (R / t) * (1 - np.cos(t * a / R))
    else:
        x = (R / t) * np.sin(t * PI / 2) + np.cos(t * PI / 2) * (a - M)
        y = (R / t) * (1 - np.cos(t * PI / 2)) + np.sin(t * PI / 2) * (a - M)
    return x, y


def make_pencil():
    w = 0.22
    cone = Polygon(ORIGIN, np.array([-w / 2, 0.40, 0]), np.array([w / 2, 0.40, 0]))
    cone.set_fill("#D2B48C", opacity=1)
    cone.set_stroke(BLACK, width=1)

    lead = Polygon(ORIGIN, np.array([-w * 0.2, 0.14, 0]), np.array([w * 0.2, 0.14, 0]))
    lead.set_fill(GREY, opacity=1)
    lead.set_stroke(BLACK, width=1)

    body = Rectangle(width=w, height=1.6)
    body.set_fill("#FFC107", opacity=1)
    body.set_stroke(BLACK, width=1)
    body.move_to(np.array([0, 1.20, 0]))

    ferrule = Rectangle(width=w, height=0.14)
    ferrule.set_fill("#9E9E9E", opacity=1)
    ferrule.set_stroke(BLACK, width=1)
    ferrule.move_to(np.array([0, 2.07, 0]))

    eraser = Rectangle(width=w, height=0.20)
    eraser.set_fill("#FF8A95", opacity=1)
    eraser.set_stroke(BLACK, width=1)
    eraser.move_to(np.array([0, 2.24, 0]))

    return VGroup(cone, lead, body, ferrule, eraser)


def fold_homotopy(x, y, z, t):
    a = -y
    bx, by = _half_bend(abs(a), t)
    if a < 0:
        bx = -bx
    top_y = _half_bend(L / 2.0, t)[1]
    upright = np.array([bx, by - top_y / 2.0, 0.0])
    return np.array([upright[1], -upright[0], 0.0])


class WormHole(Scene):
    def construct(self):
        sheet = ParametricFunction(
            lambda s: (s - L / 2.0) * DOWN,
            t_min=0,
            t_max=L,
            num_anchor_points=240,
            color=BLUE,
        )
        sheet.set_stroke(width=6)

        self.play(ShowCreation(sheet), run_time=2)
        self.wait(0.5)

        self.play(Homotopy(fold_homotopy, sheet), run_time=2, rate_func=smooth)
        self.wait(0.5)

        pencil = make_pencil()
        pencil.scale(2)
        x_off = 0.7
        pencil.move_to(np.array([x_off, FRAME_Y_RADIUS + pencil.get_height() / 2.0, 0]))
        self.play(
            pencil.move_to, np.array([x_off, -0.15, 0]),
            rate_func=smooth,
            run_time=2.5,
        )
        self.wait(2)

        self.play(
            Indicate(
                sheet,
                color=YELLOW,
                scale_factor=1.15,
            )
        )
        self.wait(2)

        # Indicate the pencil with NO colour change -- just a grow-and-shrink
        # pulse.
        self.play(
            ApplyMethod(
                pencil.scale, 1.15, rate_func=there_and_back,
            )
        )
        self.wait(2)

        self.play(FadeOut(VGroup(sheet, pencil)))
        self.wait(0.5)
