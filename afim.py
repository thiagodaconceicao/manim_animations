from manim import *

class Equation(Scene):
  def construct(self):
      text=MathTex("y=x^2-7x+10")                #variael equação# 
      self.add(text)
      self.play(Write(text))                     #função para desenhar a equação#
      self.play(text.animate.to_edge(UP))        #subir a equação#
      self.play(text.animate.to_edge(LEFT))      #move a equação para a esquerda#

      text2=Tex(r"A=1","B=-7","C=10")            #variavel resultado da primeira equação#
      self.add(text2)
      self.play(Write(text2))                    #escrevendo a equação2#
      self.play(text2.animate.to_edge(UP))       #movendo a equação2 para cima#
      
      text3=MathTex("\Delta=(-7)^2-4.1.10")      #equação delta#
      self.add(text3)
      self.play(Write(text3))                    #escrever a equação delta#
      
      self.play(Unwrite(text))                   #apagar a primeira equação#
     
      self.play(text2.animate.to_edge(LEFT))     #mover a segunda equação para a esquerda#
      self.play(text3.animate.to_edge(UP))       #mover o delta para cima#
      
      text4=MathTex("\Delta=49-40 ","=","\Delta=9") #calculo de delta#
      self.add(text4)
      self.play(Write(text4))                    #escrever o calculo#

      self.play(Unwrite(text2))                  #apagar a segunda equação#

      self.play(text3.animate.to_edge(LEFT))     #mover a eqquação delta para a esquerda#
      self.play(text4.animate.to_edge(UP))       #mover o calculo de delta para cima#
 
      self.play(Unwrite(text3))                  #apagar a equação a equação delta#
      self.play(Unwrite(text4))                  #apagar o resultado de delta#

      text5=Tex(r"$X_{v}=\frac{7}{2.1}=\frac{7}{2}$")  #Coodernadas 1#
      self.add(text5)
      self.play(Write(text5))
      self.play(text5.animate.to_edge(UP))
      
      text6=Tex(r"$Y_{v}=\frac{-9}{4.1}=\frac{-9}{4}$") #Coodernadas 2#
      self.add(text6)
      self.play(Write(text6))
 
      self.play(Unwrite(text5))
      self.play(Unwrite(text6))

      text7=Tex(r"$x=\frac{7 \pm \sqrt{9}}{2.1}=\frac{7 \pm 3}{2}$")
      self.add(text7)
      self.play(Write(text7))

      self.play(text7.animate.to_edge(UP))

      text8=Tex(r"$X_{1}=\frac{10}{2}=5$")
      self.add(text8)
      self.play(Write(text8))
      self.play(text8.animate.to_edge(LEFT))

      text9=Tex(r"$X_{2}=\frac{4}{2}=2$")
      self.add(text9)
      self.play(Write(text9))      
      self.play(text9.animate.to_edge(RIGHT))

      text10=Tex(r"$V_{1}(\frac{7}{2},\frac{-9}{4})$")
      self.add(text10)
      self.play(Write(text10))
      self.play(text10.animate.to_edge(DOWN))
      self.play(text10.animate.to_edge(LEFT))


      text11=Tex(r"$V_{2}(\frac{3}{5},\frac{-2}{2})$")
      self.add(text11)
      self.play(Write(text11))
      self.play(text11.animate.to_edge(DOWN))
      self.play(text11.animate.to_edge(RIGHT))
      
      text12=Tex(r"Obrigado por assistir")
      self.add(text12)
      self.play(Write(text12))

      self.play(Unwrite(text7))
      self.play(Unwrite(text8))
      self.play(Unwrite(text9))
      self.play(Unwrite(text10))
      self.play(Unwrite(text11))
      self.play(Unwrite(text12))


      self.wait(2)
