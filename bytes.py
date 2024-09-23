from manim import *
class join(Scene):
    def construct(self):
        r1 = Rectangle(height=1,width=0.98).scale(0.8).shift(UL*2).shift(LEFT*4.3)
        r2= Rectangle(height=1, width=5.2).scale(0.8).next_to(r1, RIGHT, buff=0)
        r3= Rectangle(height =1, width=1.75).scale(0.8).next_to(r2, RIGHT, buff= 0)
        r4= Rectangle(height =1, width=1.75).scale(0.8).next_to(r3, RIGHT, buff= 0)
        r5= Rectangle(height =1, width=1.75).scale(0.8).next_to(r4, RIGHT, buff= 0)
        r6= Rectangle(height =1, width=1.75).scale(0.8).next_to(r5, RIGHT, buff= 0)
        r7= Rectangle(height =1, width=1.8).scale(0.8).next_to(r6, RIGHT, buff= 0)
        str1= Text('0',font = "Monospace").move_to(r1).scale(0.4)
        str2 = Text('Free Spacee', font= "Monospace").move_to(r2).scale(0.3)
        str3 = Text('A5', font = "Monospace").scale(0.3).move_to(r3).set_color(PURPLE_B)
        str4 = Text('A4', font= "MOnospace").scale(0.3).move_to(r4).set_color(ORANGE)
        str5 = Text('A3', font="Monospace").scale(0.3).move_to(r5).set_color(GREEN_C)
        str6 = Text('A2', font= "Monospace").scale(0.3).move_to(r6).set_color(BLUE_D)
        str7 = Text('A1', font= "Monospace").scale(0.3).move_to(r7).set_color(RED)
        r8 = Rectangle(height=1, width=14.98).scale(0.8).next_to(r1, DOWN, buff=2).shift(RIGHT*5.61)
        a1 = Arrow(UP,DOWN,max_tip_length_to_length_ratio=0.11,stroke_width=2.5).scale(1.6).next_to(r2,DOWN).shift(UP*0.4)
        a2= Arrow(UP,DOWN,max_tip_length_to_length_ratio=0.11,stroke_width=2.5).scale(1.6).next_to(r3,DOWN).shift(UP*0.4).shift(RIGHT*0.05)
        a3 = Arrow(UP,DOWN,max_tip_length_to_length_ratio=0.11,stroke_width=2.5).scale(1.6).next_to(r4,DOWN).shift(UP*0.4).shift(RIGHT*0.05)
        a4 = Arrow(UP,DOWN,max_tip_length_to_length_ratio=0.11,stroke_width=2.5).scale(1.6).next_to(r5,DOWN).shift(UP*0.4).shift(RIGHT*0.05)
        a5 = Arrow(UP,DOWN,max_tip_length_to_length_ratio=0.11,stroke_width=2.5).scale(1.6).next_to(r6,DOWN).shift(UP*0.4).shift(RIGHT*0.05)
        a6 = Arrow(UP,DOWN,max_tip_length_to_length_ratio=0.11,stroke_width=2.5).scale(1.6).next_to(r7,DOWN).shift(UP*0.4).shift(RIGHT*0.05)
        str8 = Text('12bytes', font = "Monospace").next_to(a1, DOWN, buff = 0.6).scale(0.3)
        str9 = Text('4bytes', font= "Monospace").next_to(a2, DOWN, buff =0.6).scale(0.3).set_color(PURPLE_B).shift(RIGHT*0.05)
        str10 = Text('4bytes', font = "Monospace").next_to(a3, DOWN, buff =0.6).scale(0.3).set_color(ORANGE)
        str11 = Text('4bytes', font = "Monospace").next_to(a4, DOWN, buff = 0.6).scale(0.3).set_color(GREEN_C)
        str12 = Text('4bytes', font = "Monospace").next_to(a5, DOWN, buff = 0.6).scale(0.3).set_color(BLUE_D)
        str13 = Text('4bytes', font = "Monospace").next_to(a6, DOWN, buff = 0.6).scale(0.3).set_color(RED)
        str14 = Text('0x000000000000000000000000', font= "Monospace", font_size=39).scale(0.5).next_to(str2, DOWN, buff = 2.59).shift(RIGHT*-0.2)
        str15 = Text('00000000', font = "Monospace", font_size=39).next_to(str3,DOWN,  buff = 2.5).scale(0.5).shift(RIGHT*-0.0000001)
        str16 = Text('00000000', font = "Monospace", font_size=39).next_to(str4, DOWN, buff = 2.5).scale(0.5).shift(RIGHT*0.005)
        str17 = Text('00000000', font = "Monospace", font_size=39).next_to(str5, DOWN, buff = 2.5).scale(0.5).shift(RIGHT*0.005)
        str18 = Text('00000000', font = "Monospace", font_size=39).next_to(str6, DOWN, buff = 2.5).scale(0.5).shift(RIGHT*0.005)
        str19 = Text('00000000', font = "Monospace", font_size=39).next_to(str7, DOWN, buff = 2.5).scale(0.5).shift(RIGHT*-0.03)
        group = VGroup(r1,r2,r3,r4,r5,r6,r7,str1,str2,str3,str4,str5,str6,str7,r8,a1,a2,a3,a4,a5,a6,str8,str9,str10,str11,str12,str13,str14,str15,str16,str17,str18,str19).move_to(0)
        
        str15_2 = Text('165CD37b', font = "Monospace", font_size=39).next_to(str3,DOWN,  buff = 2.5).scale(0.5).shift(RIGHT*-0.0000001).set_color(PURPLE_A)
        str16_2 = Text('b4C644C2', font = "Monospace", font_size=39).next_to(str4, DOWN, buff = 2.5).scale(0.5).shift(RIGHT*0.005).set_color(ORANGE)
        str17_2 = Text('92145442', font = "Monospace", font_size=39).next_to(str5, DOWN, buff = 2.5).scale(0.5).shift(RIGHT*0.005).set_color(GREEN_C)
        str18_2 = Text('9E7F9358', font = "Monospace", font_size=39).next_to(str6, DOWN, buff = 2.5).scale(0.5).shift(RIGHT*0.005).set_color(BLUE_D)
        str19_2 = Text('ed89AbdE', font = "Monospace", font_size=39).next_to(str7, DOWN, buff = 2.5).scale(0.5).shift(RIGHT*-0.03).set_color(RED)
        
        self.play(FadeIn(VGroup(r1,r2,r3,r4,r5,r6,r7,str1,str2,str3,str4,str5,str6,str7)))
        self.play(FadeIn(str14,r8,str15,str16,str17,str18,str19))
        
        
        self.play(Write(a6))
        self.play(TransformFromCopy(str7.copy(), str19_2))
        self.play(ReplacementTransform(str19, str19_2), run_time=0.01)
        self.play(FadeIn(str13))
        
        self.play(Write(a5))
        self.play(TransformFromCopy(str6.copy(), str18_2))
        self.play(ReplacementTransform(str18, str18_2), run_time=0.01)
        self.play(FadeIn(str12))
        
        self.play(Write(a4))
        self.play(TransformFromCopy(str5.copy(), str17_2))
        self.play(ReplacementTransform(str17, str17_2), run_time=0.01)
        self.play(FadeIn(str11))
        
        self.play(Write(a3))
        self.play(TransformFromCopy(str4.copy(), str16_2))
        self.play(ReplacementTransform(str16, str16_2), run_time=0.01)
        self.play(FadeIn(str10))
        
        self.play(Write(a2))
        self.play(TransformFromCopy(str3.copy(),str15_2))
        self.play(ReplacementTransform(str15, str15_2), run_time=0.01)
        self.play(FadeIn(str9))
        
        self.play(Write(a1))
        self.play(Transform(VGroup(str2).copy(),str14.copy()))#,FadeOut(str14))
        self.play(FadeIn(str8))
        
        
        

       
        
        
       
       
       
       
        
        
        
        
        self.wait(2)
        #self.add(,r8,a1,a2,a3,a4,a5,a6,str8,str9,str10,str11,str12,str13,str14,str15,str16,str17,str18,str19,group)
        