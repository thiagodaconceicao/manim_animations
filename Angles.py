from manim import *
import numpy as np

class Angles(Scene):
    def construct(self):
        title = Text("Ângulos:", font_size=48, color=WHITE)
        title.to_edge(UP, buff=0.5)  

        self.play(Create(title))

        circle = Circle(radius=2)
        self.play(Create(circle))
        
        line = Line(circle.get_center(), circle.point_from_proportion(1), color=BLUE)
        self.play(Create(line))
        
        dot_start = Dot(circle.get_center(), color=BLUE)
        dot_end = Dot(circle.point_from_proportion(1), color=GREEN)

        self.add(dot_start, dot_end)
        
        angles = [30, 90, 180, 270, 360]  

        for angle_value in angles:
            angle = Arc(start_angle=0, angle=angle_value * DEGREES)
            self.play(Create(angle))
            
            angle_label = Tex(f"{angle_value}°")
            
          
            radius = circle.get_width() / 2
            label_radius = radius + 0.5  
            label_angle = angle_value * DEGREES
            label_x = np.cos(label_angle) * label_radius
            label_y = np.sin(label_angle) * label_radius
            label_position = circle.get_center() + np.array([label_x, label_y, 0])
            
            angle_label.move_to(label_position)
            self.play(Create(angle_label))

        self.wait(2)
