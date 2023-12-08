from manim import *

class scene(Scene):
    def construct(self):
        num=NumberPlane()
        cir=Circle(radius=3,color=WHITE)
        x=ValueTracker(0)
        line1=Line([10,0,0],[-10,0,0],color=YELLOW)
        line2=Line([0,10,0],[0,-10,0],color=YELLOW)
        radius=VMobject()
        dot=VMobject()
        sin=VMobject()
        cos=VMobject()
        angle=VMobject()
        tangent=VMobject()
        sinb=VMobject()
        cosb=VMobject()
        text=VMobject()
        grp=VGroup(sinb,cosb)
        mgrp=VGroup(radius,dot,sin,cos,angle,tangent,text)
        sint=Text("Sin r\theta")
        cost=Text("Cos r\theta")
        tant=Text("Tan r\theta")
        text_group=VGroup(sint,cost,tant)

        def get_coord(list,index):
            return list[index]

        def get_stuff(mgrp):
            xx=x.get_value()
            r=radius
            d=dot
            s=sin
            c=cos
            a=angle
            t=tangent
            tex=text
            r.become(Line([0,0,0],cir.point_at_angle(xx)))
            d.become(Dot(cir.point_at_angle(xx)))
            s.become(Line(cir.point_at_angle(xx),[get_coord(cir.point_at_angle(xx),0),0,0],color=RED))
            c.become(Line([0,0,0],[get_coord(cir.point_at_angle(xx),0),0,0],color=RED))
            a.become(Arc(radius=0.3,angle=xx))
            t.become(Line([3/np.cos(xx),0,0],[0,3/np.sin(xx),0],color=BLUE))
            tex.become(MathTex(r"\theta").move_to(Arc(radius=0.3+3*SMALL_BUFF,angle=xx).point_from_proportion(0.5)))


        def get_text(text_group):
            s=sint
            c=cost
            t=tant
            xx=x.get_value()
            s.become(MathTex(r"\sin(\theta)")
                    .move_to(
                        Line(cir.point_at_angle(xx),[get_coord(cir.point_at_angle(xx),0),0,0]).point_from_proportion(0.5),LEFT
                        ))
            c.become(MathTex(r"\cos(\theta)")
                    .move_to(
                        Line([0,0,0],[get_coord(cir.point_at_angle(xx),0),0,0]).point_from_proportion(0.5),DOWN
                        ))
            t.become(MathTex(r"\tan(\theta)")
                    .move_to(
                        Line(cir.point_at_angle(xx),[3/np.cos(xx),0,0]).point_from_proportion(0.5),RIGHT
                        ))

        mgrp.add_updater(get_stuff)
        text_group.add_updater(get_text)

        self.add(num,cir,line1,line2,mgrp,text_group)
        self.play(x.animate(rate_func=linear).set_value(PI*2),run_time=10)