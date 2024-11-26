import pygame


def scale_image(a,b):
   size=round(a.get_width()*b),round(a.get_height()*b)
   return pygame.transform.scale(a,size)