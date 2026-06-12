from manim import *

class deemo(Scene):
    def construct(self):

        #-----Objects-----

        i = MathTex(
            "i",
            font_size=300
        )

        assumptions = Text(
            "Assumptions:",
            font_size=50
        ).move_to([-4.5, 3.25, 0])

        line = Line(
            [-6.7, 2.75, 0],
            [6.7, 2.75, 0],
            stroke_width=6
        )

        line2 = Line(
            [-1.2, 2.76, 0],
            [-1.2, -3.5, 0],
            stroke_width=6
        )
        
        line3 = VGroup(line, line2)

        iSquared = MathTex(
            "i^2 = -1",
            font_size=150
        ).move_to([3, 0, 0])

        nLine = (
            NumberLine(
                x_range = [-4, 4, 1],
                length = 6,
                numbers_to_exclude=[-4],
                include_numbers=True,
                include_tip=True
            )
            .add_tip(at_start=True)
            .move_to([3, 0, 0])
        )
        
        nPlane = Axes(
            x_range=[-4, 4, 1],
            x_length=5.7,
            y_range=[-4, 4, 0.8],
            y_length=5.7,
            axis_config={"include_tip": True},
            x_axis_config={"include_numbers": True, "numbers_to_exclude": [-4]},
        ).move_to([3, -0.675, 0])

        nPlane.get_x_axis().add_tip(
            at_start=True
        )
        nPlane.get_y_axis().add_tip(
            at_start=True
        )
        nPlane.get_y_axis().add_labels(
            {-3: "-3i", -2: "-2i", -1: "-i", 1: "i", 2: "2i", 3: "3i"},
            direction=RIGHT,
        )
        nPlane.get_y_axis().labels.shift(
            UP * 0.2
        )

        iMath = MathTex(
            "(1+i)^2", "=", "1+2i", "+ i^2",
            font_size = 75
        ).move_to([3, 0, 0])

        Negative1 = MathTex(
            "-1",
            font_size = 75
        )

        Twoi = MathTex(
            "2i",
            font_size = 75
        )

        i0 = VGroup(iSquared, iMath, Negative1, Twoi)

        Plane = NumberPlane(
            x_range=[-14, 14, 1],
            x_axis_config={"include_numbers": True}
        ).move_to([0.175, 0, 0])
        Plane.get_y_axis().add_labels(
            {-4: "-4i", -3: "-3i", -2: "-2i", -1: "-i", 1: "i", 2: "2i", 3: "3i", 4: "4i"},
            direction=RIGHT,
        )
        Plane.get_y_axis().labels.shift(
            DOWN * 0.2
        )



        #-----Scenes-----

        self.play(
            Write(
                i
            )
        )

        self.wait()

        self.play(
            i.animate.move_to([-2.05, 3.32, 0])
            .scale(0.275),
            Write(assumptions),
            Create(line3)
        )

        self.wait()

        self.play(
            Write(
                iSquared
            )
        )

        self.play(
            iSquared.animate.move_to([-4.1, 1.3, 0])
            .scale(0.7)
        )

        self.wait()



        self.wait()

        self.play(
            Write(
                iMath
            )
        )

        self.wait(0.25)

        self.play(
            Indicate(
                iMath[3],
                1.2,
                color=WHITE,
                run_time = 0.5
            )
        )

        self.wait(0.25)

        Negative1.move_to([5.7, 0, 0])

        self.play(
            Transform(
                iMath[3],
                Negative1
            )
        )

        self.wait(0.25)

        i34 = VGroup(iMath[2], iMath[3], Negative1)

        Twoi.move_to([3.5, 0, 0])

        self.play(
            Transform(
                i34,
                Twoi
            )
        )

        self.wait()

        ia = VGroup(iMath, Negative1, i34, Twoi)

        self.play(
            ia.animate.move_to([-4.05, -2, 0])
            .scale(1)
        )

        self.wait()

        self.play(
            Create(
                nPlane,
                run_time=2
            )
        )

        self.wait(2)

        slide1 = VGroup(i, assumptions, line3, nPlane, i0)
        
        self.play(
            slide1.animate.move_to([-14.5, 0, 0]),
        )

        self.play(
             Write(Plane)
        )

      


class deeemo(Scene):
    def construct(self):

        #-----Objects-----

        Plane = NumberPlane(
            x_range=[-14, 14, 1],
            x_axis_config={"include_numbers": True}
        ).move_to([0.175, 0, 0])
        Plane.get_y_axis().add_labels(
            {-4: "-4i", -3: "-3i", -2: "-2i", -1: "-i", 1: "i", 2: "2i", 3: "3i", 4: "4i"},
            direction=RIGHT,
        )
        Plane.get_y_axis().labels.shift(
            DOWN * 0.2
        )
        
        d1 = Dot(
            [4, -1, 0],
            color = PURPLE,
        ).scale(1.325)

        d2 = Dot(
            [-2, 2, 0],
            color = YELLOW,
        ).scale(1.325)

        arrow1 = always_redraw(
            lambda: (
                Line(
                    start=Plane.get_origin(),
                    end=d1.get_center() -
                    normalize(d1.get_center() - Plane.get_origin()) * 0.25,
                    buff=0
                )
                .add_tip(tip_shape=ArrowTriangleFilledTip)
            )
        )

        arrow2 = always_redraw(
            lambda: (
                Line(
                    start=Plane.get_origin(),
                    end=d2.get_center() -
                    normalize(d2.get_center() - Plane.get_origin()) * 0.25,
                    buff=0
                )
                .add_tip(tip_shape=ArrowTriangleFilledTip)
            )
        )

        v1 = MathTex(
            "(4-", "i", ")",
            font_size = 40
        ).move_to([4, -0.5, 0])

        v2 = MathTex(
            "(-2+", "2i", ")",
            font_size = 40
        ).move_to([-2, 2.5, 0])
        
        v3 = MathTex(
            "(2+", "i", ")",
            font_size = 40
        ).move_to([2, 1.5, 0])

        v3t = VGroup(v1, v2)

        p1 = VGroup(d1, v1)
        p2 = VGroup(d2, v2)

        r = Rectangle(
            height = 7,
            width = 5,
            color = WHITE,
            fill_opacity = 1,
            fill_color = BLACK
        ).move_to([3.5, 0, 0])

        m1 = MathTex("(4-i)+(-2+2i)").move_to([3.5, 2.75, 0])

        m2 = MathTex("4-i-2+2i").move_to([3.5, 1.375, 0])

        m3 = MathTex("4-2", "2i-i").move_to([3.5, 0, 0])

        m4 = MathTex("2", "i").move_to([3.5, -1.375, 0])

        m5 = MathTex("2+i").move_to([3.5, -2.75, 0])

        l = Line(
            [3.5, 0.5, 0],
            [3.5, -1.875, 0]
        )

        sr = SurroundingRectangle(m5)

        al = VGroup(m1, m2, m3, m4, m5, l, sr)

        all = VGroup(Plane, arrow1, arrow2, d1, d2, v3[0], v3[2])
        
        alll = VGroup(p1, p2, Plane)

        #-----Scenes-----


        self.add(Plane)

        Plane.set_z_index(-1)

        self.wait()

        self.play(
            Create(d1),
            Create(d2)
        )
        self.play(
            Write(arrow1),
            Write(arrow2),
            Write(v1),
            Write(v2)
        )

        self.wait(2)

        self.play(
            Indicate(v2[1]),
            Indicate(v1[1])
        )

        self.wait(2)

        self.play(
            alll.animate.shift(LEFT * 4)
        )

        #-----Box-----

        self.play(
            DrawBorderThenFill(
                r
            )
        )

        m3[0].shift(LEFT * 0.6)
        m3[1].shift(RIGHT * 0.65)
        m4[0].shift(LEFT * 1)
        m4[1].shift(RIGHT * 1)

        self.play(Write(m1))
        self.play(Write(m2))
        self.play(Write(m3), Write(l))
        self.play(Write(m4))
        self.wait()
        self.play(Write(m5), Write(sr))

        self.wait(2)

        self.play(
            Unwrite(
                al,
                run_time = 1
            ),
            Unwrite(r)
        )

        self.play(
            alll.animate.shift(RIGHT * 4)
        )

        self.wait()

        self.play(
            d1.animate.move_to([2, 1, 0]).set_color(GREEN),
            d2.animate.move_to([2, 1, 0]).set_color(GREEN),
            ReplacementTransform(v3t, v3),
        )

        self.wait()

        self.play(
            FadeOut(all)
        )

        self.play(
            v3[1].animate.move_to([0, 0, 0]).scale(10)
        )




class deeeemo(Scene):
    def construct(self):

        #-----Objects-----

        Plane = NumberPlane(
            x_range=[-14, 14, 1],
            x_axis_config={"include_numbers": True}
        ).move_to([0.175, 0, 0])
        Plane.get_y_axis().add_numbers([-4, -3, -2, -1, 1, 2, 3, 4])
        y_numbers = Plane.get_y_axis().numbers

        i = MathTex("i").scale(10)

        d1 = Dot(
            [3, 2, 0],
            color = PURPLE,
        ).scale(1.325)

        d2 = Dot(
            [3, 2, 0],
            color = RED,
            stroke_color=BLACK,
            stroke_width=1
        ).scale(1.6)

        d3 = Dot(
            [-2, 3, 0],
            color = ORANGE,
            stroke_color=BLACK,
            stroke_width=1
        ).scale(1.6)
        
        d4 = Dot(
            [-3, -2, 0],
            color = BLUE,
            stroke_color=BLACK,
            stroke_width=1
        ).scale(1.6)

        d5 = Dot(
            [2, -3, 0],
            color = GREEN,
            stroke_color=BLACK,
            stroke_width=1
        ).scale(1.6)

        v1 = always_redraw(
            lambda: (
                MathTex("(3,2)", font_size = 40).move_to([d1.get_x(), d1.get_y() + 0.5, 0])
            )
        )
        v01 = MathTex("(3,2)", font_size = 40).move_to([3.25, 3, 0])

        v2 = always_redraw(
            lambda: (
                MathTex("(-2,3)", font_size = 40).move_to([d1.get_x(), d1.get_y() + 0.5, 0])
            )
        )
        v02 = MathTex("(-2,3)", font_size = 40).move_to([-2.5, 3.5, 0])

        v3 = always_redraw(
            lambda: (
                MathTex("(-3,-2)", font_size = 40).move_to([d1.get_x(), d1.get_y() + 0.5, 0])
            )
        )
        v03 = MathTex("(-3,-2)", font_size = 40).move_to([-3.5, -2.5, 0])

        v4 = always_redraw(
            lambda: (
                MathTex("(2,-3)", font_size = 40).move_to([d1.get_x(), d1.get_y() + 0.5, 0])
            )
        )
        v04 = MathTex("(2,-3)", font_size = 40).move_to([2.5, -3.5, 0])

        yl = Line(
            [0.02, 10, 0],
            [0.02, -10, 0],
            stroke_width = 3.5
        ) 
        
        op = ValueTracker(1)

        l1 = always_redraw(
            lambda: (
                Line(
                    [0.0, 0, 0],
                    [d1.get_x(), 0, 0],
                    color = YELLOW,
                    stroke_width = 7.5
                ).set_opacity(op.get_value())
            )
        )

        a1 = always_redraw(
            lambda: (
                Line(
                    [d1.get_x(), 0, 0],
                    [d1.get_x(), d1.get_y() - 0.25, 0],
                    color = YELLOW,
                    stroke_width = 7.5
                ).add_tip(tip_shape=ArrowTriangleFilledTip).set_opacity(op.get_value())
            )
        )

        la1 = VGroup(l1, a1)

        arrow = always_redraw(
            lambda: (
                Line(
                    start=Plane.get_origin(),
                    end=d1.get_center() -
                    normalize(d1.get_center() - Plane.get_origin()) * 0.25,
                    buff=0,
                    color = BLUE,
                    stroke_width = 7.5
                )
                .add_tip(tip_shape=ArrowTriangleFilledTip)
            )
        )

        trail = TracedPath(d1.get_center, stroke_color=WHITE, stroke_width=5)
        ra = ValueTracker(0.5)
        circle = always_redraw(
            lambda: (
                Circle(radius=ra.get_value(), color=YELLOW)
            )
        )
        
        dashed_circle = always_redraw(
            lambda: (
                DashedVMobject(circle, num_dashes=50, dashed_ratio=0.5)
            )
        )

        recl = ValueTracker(5)

        r = always_redraw(
            lambda: (
                Rectangle(
                    height = recl.get_value(),
                    width = 3,
                    color = WHITE,
                    fill_opacity = 1,
                    fill_color = BLACK
                ).move_to([5.4, 0, 0])
            )
        )

        #-----Degree BS-----

        start_angle = angle_of_vector(d1.get_center())
        theta = ValueTracker(0)

        angle_arc = always_redraw(
              lambda: DashedVMobject(
                  Arc(
                      radius=1,
                      start_angle=start_angle,
                      angle=max(theta.get_value(), 1e-3),
                      arc_center=ORIGIN,
                      color=WHITE,
                  ),
                  num_dashes=20,
              )
          )
        
        deg_label = always_redraw(
              lambda: DecimalNumber(
                  theta.get_value() * 180 / PI,          
                  num_decimal_places=0,
                  unit="^\\circ",
                  font_size=36,
              ).move_to([-0.35, 1.25, 0])                    
          )


        #-----Scenes-----

        self.add(i)

        self.wait(2)

        self.play(
            ReplacementTransform(i, v1, run_time = 1.5),
            Write(Plane),
            Write(yl),
            Create(d1)
        )
        
        Plane.set_z_index(-1)
        yl.set_z_index(10)

        self.play(
            Write(la1)
        )

        self.wait()

        self.play(
            op.animate.set_value(0.4),
            Write(arrow)
        )

        self.wait()

        #-----Full CIrcle Cycle-----

        self.play(Create(dashed_circle))
        self.play(ra.animate.set_value(3.6055))    

        self.add(angle_arc, deg_label)
        self.add(trail)
        self.play(Rotate(d1, angle=PI/2, about_point=ORIGIN),
              theta.animate.set_value(PI/2), Write(v01), Create(d2))
        d2.set_z_index(25)
        
        v2.move_to([d1.get_x(), d1.get_y() + 0.5, 0])
        self.play(ReplacementTransform(v1, v2))


        self.wait(0.5)


        self.play(Rotate(d1, angle=PI/2, about_point=ORIGIN),
              theta.animate.set_value(PI), Write(v02), Create(d3))
        
        v3.move_to([d1.get_x(), d1.get_y() + 0.5, 0])
        self.play(ReplacementTransform(v2, v3))


        self.wait(0.5)


        self.play(Rotate(d1, angle=PI/2, about_point=ORIGIN),
              theta.animate.set_value(1.5*PI), Write(v03), Create(d4))
        
        v4.move_to([d1.get_x(), d1.get_y() + 0.5, 0])
        self.play(ReplacementTransform(v3, v4))


        self.wait(0.5)


        self.play(Rotate(d1, angle=PI/2, about_point=ORIGIN),
              theta.animate.set_value(2*PI), Write(v04), FadeOut(v4), Create(d5))

        self.remove(v4)
        self.wait(0.5)


        #-----End Full Circle Cycle-----

        self.play(Write(r))
        r.set_z_index(-1)
        self.play(
            v01.animate.move_to([5.25, 2, 0]),
            v02.animate.move_to([5.25, 0.666666, 0]),
            v03.animate.move_to([5.25, -0.666666, 0]),
            v04.animate.move_to([5.25, -2, 0])
        )

        self.wait()

        self.play(Indicate(v01))
        self.play(Indicate(v02))
        self.play(Indicate(v03))
        self.play(Indicate(v04))

        self.wait()

        v001 = MathTex("(a,b)", font_size = 40).move_to([v01.get_x(), v01.get_y(), 0])
        v002 = MathTex("(-b,a)", font_size = 40).move_to([v02.get_x(), v02.get_y(), 0])
        v003 = MathTex("(-a,-b)", font_size = 40).move_to([v03.get_x(), v03.get_y(), 0])
        v004 = MathTex("(b,-a)", font_size = 40).move_to([v04.get_x(), v04.get_y(), 0])

        self.play(
            TransformMatchingTex(v01, v001),
            TransformMatchingTex(v02, v002),
            TransformMatchingTex(v03, v003),
            TransformMatchingTex(v04, v004)
        )

        self.wait()

        self.play(
            Unwrite(v003, run_time = 0.5),
            Unwrite(v004, run_time = 0.5),
        )

        self.play(
            v001.animate.move_to([5.25, 0.66666, 0]),
            v002.animate.move_to([5.25, -0.66666, 0]),
            recl.animate.set_value(3)
        )

        self.wait(2)

        everything = VGroup(
            d3, d4, d5,
            v001, v002,
            la1, arrow, trail,
            dashed_circle, r,
            angle_arc, deg_label
          )
        
        self.play(FadeOut(everything))




class deeeeemo(Scene):
    def construct(self):

        #-----Objects-----

        Plane = NumberPlane(
            x_range=[-14, 14, 1],
            x_axis_config={"include_numbers": True}
        ).move_to([0.175, 0, 0])
        Plane.get_y_axis().add_numbers([-4, -3, -2, -1, 1, 2, 3, 4])
        y_numbers = Plane.get_y_axis().numbers

        yl = Line(
            [0.02, 10, 0],
            [0.02, -10, 0],
            stroke_width = 3.5
        )

        d1 = Dot(
            [3, 2, 0],
            color = RED,
            stroke_color=BLACK,
            stroke_width=1
        ).scale(1.6)

        d2 = Dot(
            [3, 2, 0],
            color = BLUE,
            stroke_color=BLACK,
            stroke_width=1
        ).scale(1.6)

        d3 = Dot(
            [-2, 3, 0],
            color = GREEN,
            stroke_color=BLACK,
            stroke_width=1,
        ).scale(1.6)

        ve = MathTex("=", font_size = 80).move_to([1.85, -2.25, 0])
        v1 = MathTex("(3,2)", font_size = 40).move_to([3.6, 2.4, 0])
        v2 = MathTex("(3+2i)", font_size = 40).move_to([3.75, 2.4, 0])
        dv2 = MathTex("(3+2i)", font_size = 40).move_to([3.75, 2.4, 0])
        dvv2 = MathTex("(3+2i)", font_size = 80).move_to([3.625, -2.25, 0])
        v3 = MathTex("i(3+2i)", font_size = 80).move_to([3.625, -2.25, 0])
        v4 = MathTex("3i+2i^2", font_size = 80).move_to([4, -2.2, 0])
        v5 = MathTex("3i+2i^2", font_size = 80).move_to([4, -2.2, 0])
        v6 = MathTex("3i-2", font_size = 80).move_to([4, -2.25, 0])
        v7 = MathTex("-2+3i", font_size = 80).move_to([4, -2.25, 0])
        dv7 = MathTex("(-2+3i)", font_size = 40).move_to([-3, 3.35, 0])

        sr = SurroundingRectangle(v7)

        r = Rectangle(
                height = 2.5,
                width = 5.5,
                color = WHITE,
                fill_opacity = 1,
                fill_color = BLACK
            ).move_to([3.75, -2.25, 0])

        arrow = always_redraw(
            lambda: (
                Line(
                    start=Plane.get_origin(),
                    end=d1.get_center() -
                    normalize(d1.get_center() - Plane.get_origin()) * 0.25,
                    buff=0
                )
                .add_tip(tip_shape=ArrowTriangleFilledTip)
            )
        )

        #-----Trail Bs-----

        trail = TracedPath(d1.get_center, stroke_color=WHITE, stroke_width=5)

        start_angle = angle_of_vector(d1.get_center())
        theta = ValueTracker(0)

        angle_arc = always_redraw(
              lambda: DashedVMobject(
                  Arc(
                      radius=1,
                      start_angle=start_angle,
                      angle=max(theta.get_value(), 1e-3),
                      arc_center=ORIGIN,
                      color=WHITE,
                  ),
                  num_dashes=20,
              )
          )
        
        deg_label = always_redraw(
              lambda: DecimalNumber(
                  theta.get_value() * 180 / PI,          
                  num_decimal_places=0,
                  unit="^\\circ",
                  font_size=36,
              ).move_to([-0.35, 1.25, 0])                    
          )



        #-----Scenes-----

        self.add(
            Plane,
            yl,
            d1
        )
        
        self.play(
            Write(v1),
        )

        #-----Y axis Change-----

        self.wait(3)
    
        i_labels = VGroup(*[
            MathTex(tex).match_height(num).move_to(num)
            for num, tex in zip(
                y_numbers,
                ["-4i", "-3i", "-2i", "-i", "i", "2i", "3i", "4i"]
            )
        ])

        self.play(
              TransformMatchingShapes(y_numbers, i_labels),
              TransformMatchingShapes(v1, v2)
        )


        self.wait()

        self.add(dv2)

        dv2.set_z_index(10)
        self.play(
            Write(r), 
            ReplacementTransform(dv2, dvv2),
        )

        self.add(dvv2)

        self.wait(0.6)

        self.play(ReplacementTransform(dvv2,v3))
        self.wait(1.5)
        self.play(TransformMatchingShapes(v3,v4), Write(ve))
        self.wait(0.1)
        self.play(TransformMatchingShapes(v4,v5))
        self.wait(0.2)
        self.play(TransformMatchingShapes(v5,v6))
        self.wait()
        self.play(TransformMatchingShapes(v6,v7), Write(sr))

        self.wait(2)

        self.play(Write(arrow))
        self.play(d1.animate.move_to([-2, 3, 0]), Create(d2))
        self.play(Write(dv7))

        self.wait(2)

        self.play(d1.animate.move_to([3, 2, 0]), Create(d3), Uncreate(d2))

        self.wait(4)

        self.add(angle_arc, deg_label)
        self.add(trail)
        self.play(Rotate(d1, angle=PI/2, about_point=ORIGIN),
              theta.animate.set_value(PI/2), Create(d2), Uncreate(d3))
        
        self.wait(1.5)

        all = VGroup(
            Plane, yl,
            d1,
            ve, v2, v7, dv7,
            sr, r,
            arrow, trail, angle_arc, deg_label,
            i_labels,
        )

        self.play(FadeOut(all))
        self.remove(all)

        self.wait(1)




class Eulers(Scene):
    def construct(self):

        #-----Objects-----  

        euler = MathTex("e^{\\pi i} + 1 = 0", font_size = 125)

        la = MathTex(r"z=i\theta", font_size = 70).move_to([5, 3, 0])

        i1 = MathTex(r"i=i", font_size = 60).move_to([0, -0.5, 0])
        i2 = MathTex(r"i^2=-1", font_size = 60).move_to([0, -1.16666, 0])
        i3 = MathTex(r"i^3=-i", font_size = 60).move_to([0, -1.83333, 0])
        i4 = MathTex(r"i^4=1", font_size = 60).move_to([0, -2.5, 0])
        i = VGroup(i1, i2, i3, i4)

        t1 = MathTex("(-\\theta^2)", color = BLUE)
        t2 = MathTex("(-i\\theta^3)", color = BLUE)
        t3 = MathTex("(\\theta^4)", color = BLUE)   
        t4 = MathTex("(i\\theta^5)", color = BLUE)
        t = VGroup(t1, t2, t3, t4)

        l1 = MathTex(r"e^z = 1 + z + \frac{1}{2!}z^2 + \frac{1}{3!}z^3 + \frac{1}{4!}z^4 + \frac{1}{5!}z^5 + \cdots").move_to([-6.8, 3, 0], aligned_edge=LEFT)
        l2 = MathTex(
            "e^{i\\theta}",
            "=1+i\\theta+\\frac{1}{2!}", "\:",  "(i\\theta)^2", "\,",  "+\\frac{1}{3!}", "\quad",  "(i\\theta)^3", "\:", 
            "+\\frac{1}{4!}", "(i\\theta)^4", "+\\frac{1}{5!}", "\,",  "(i\\theta)^5",  "+\\cdots"
        ).move_to([-6.8, 1, 0], aligned_edge=LEFT)
        l3 = MathTex(
            "e^{i\\theta}",
            "=",
            "\\left(",
            "1-\\frac{1}{2!}\\theta^2+\\frac{1}{4!}\\theta^4-\\cdots",
            "\\right)",
            "+i\\left(",
            "\\theta-\\frac{1}{3!}\\theta^3+\\frac{1}{5!}\\theta^5-\\cdots",
            "\\right)"
        ).move_to([-6.8, -1, 0], aligned_edge=LEFT)
        l4 = MathTex(
            "e^{i\\theta}", "=\\cos(\\theta)+i\\sin(\\theta)"
        ).move_to([-6.8, -3, 0], aligned_edge=LEFT)


        l2pi = MathTex(r"\theta = \pi")

        l22 = MathTex(r"e^{i\pi} = \cos\pi + i\sin\pi").move_to([-6.8, 1, 0], aligned_edge=LEFT)
        l23 = MathTex(r"e^{i\pi} = -1").move_to([-6.8, -1, 0], aligned_edge=LEFT)
        l24 = MathTex(r"e^{i\pi} + 1 = 0").move_to([-6.8, -3, 0], aligned_edge=LEFT)

        b1 = Brace(l3, direction = DOWN)
        bt = Text("Alternating Series").move_to([b1.get_x(), b1.get_y() - 0.5, 0])
        b = VGroup(b1, bt)

        lasr = SurroundingRectangle(la, color = WHITE)
        isr = SurroundingRectangle(i, color = WHITE)
        sr = SurroundingRectangle(l24)

        answer = VGroup(l24, sr)

        #-----Scenes-----

        self.play(Write(euler))

        self.wait()

        self.play(Unwrite(euler))

        self.play(Write(l1))

        self.wait(1.5)
        self.play(Write(la), Write(lasr))
        self.wait()
        
        self.play(Write(l2))
        self.wait(1.5)
        self.play(Write(isr), Write(i))
        self.wait(1.5)
        t1.move_to(l2[3])
        t2.move_to(l2[7])
        t3.move_to(l2[10])
        t4.move_to(l2[13])
        self.play(
            TransformMatchingShapes(l2[3], t1),
            TransformMatchingShapes(l2[7], t2),
            TransformMatchingShapes(l2[10], t3),
            TransformMatchingShapes(l2[13], t4),
            FadeOut(l2[10][1])
        )
        self.wait(1.5)

        self.play(FadeOut(i), FadeOut(isr))
        self.play(Write(l3))
        self.wait(1.5)
        self.play(Write(b1))
        self.play(Write(bt, run_time = 1))


        self.wait(1.5)

        self.play(FadeOut(b))
        self.play(Write(l4))
 
        self.wait()

        self.play(
            FadeOut(l1),
            FadeOut(
                l2[0], l2[1], l2[2], l2[4], l2[5], l2[6],
                l2[8], l2[9], l2[11], l2[12], l2[14]),
            FadeOut(l3),
            FadeOut(la),
            FadeOut(t),
            FadeOut(lasr)
        )

        self.play(l4.animate.shift(UP * 6))
        self.wait()
        self.play(Write(l22))
        self.wait()
        self.play(Write(l23))
        self.wait()
        self.play(Write(l24))
        self.play(Write(sr))
        self.wait()
        self.play(
            FadeOut(l22),
            FadeOut(l23),
            FadeOut(l4)
        )
        self.play(answer.animate.move_to([0, 0, 0]).scale(3))

        self.wait(1.5)

        self.play(FadeOut(answer))

        self.wait()




class Quaternions(Scene):
    def construct(self):

        #-----Objects----- 
        
        q = Text("Quaternion:").move_to([0, 3, 0])

        v = MathTex("1.26", "+", "3.84", "i+", "2.63", "j+", "1.92", "k",).move_to([0, 2, 0])
        v[2].set_color(RED)
        v[4].set_color(GREEN)
        v[6].set_color(BLUE)
        
        t1 = Text("Values", font_size = 40)
        t2 = Text("Scalar", color = YELLOW, font_size = 30)
        t3 = Text("Imaginary", font_size = 30)

        #-----Scenes-----

        self.play(
            Write(q),
            Write(v)
        )

        self.wait(5)

        self.play(
            q.animate.shift(DOWN * 0.5),
            v.animate.shift(DOWN *1)
        )
        
        b1 = Brace(v, DOWN)
        b12 = b1.copy()
        b2 = Brace(v[0], DOWN)
        b3 = Brace(v[2:7], DOWN)

        self.wait(0.1)
        self.play(Write(b1), Write(b12))
        t1.move_to([b1.get_x(), b1.get_y() - 0.5, 0])
        self.play(Write(t1))
        self.wait()

        b2
        self.play(
            Transform(b1, b2),
            Transform(b12, b3),
            FadeOut(t1)
        )

        t2.move_to([b2.get_x(), b2.get_y() - 0.5, 0])
        t3.move_to([b3.get_x(), b3.get_y() - 0.5, 0])
        self.play(
            Write(t2),
            Write(t3)
        )

        self.wait(2)

        all = VGroup(v, q, b2, b3, t2, t3)

        self.play(FadeOut(all))

        self.wait()
