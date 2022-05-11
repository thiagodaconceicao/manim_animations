from manim import *

class parabola(Scene):
    def construct(self):
        
        ax = Axes(
                 
   

        axis_config={"include_numbers": True})
        self.play(Create(ax))
        
          
        
       
        
        self.wait(2)
        self.add(ax)