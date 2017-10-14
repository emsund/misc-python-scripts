import sys
import pygame

size = width, height = 500, 500
degree = 0

bg = (20, 20, 20)
white = pygame.Color('white')
red = pygame.Color('red')
cyan = pygame.Color('cyan')
black = pygame.Color('black')

screen = pygame.display.set_mode(size)
screen.fill(bg)


# length of one side of equilateral triangle
s = 40

# height of equilateral triangle of side-length s
h = ((3**0.5)/2)*s

# size of smallest bounding square -> that can also share a center
m = (4/3)*h

#tri_points = [(0, 0), (tri_side_len, 0), (tri_side_len/2, tri_height)]
tri_points = [(m/2, 0), ((m-s)/2, h), ((m+s)/2, h)]

tri_surf = pygame.Surface((m,m))
tri_surf.fill(white)
tri_surf.set_colorkey(white)

tri = pygame.draw.polygon(tri_surf, red, tri_points, 2)
#tri = pygame.draw.aalines(tri_surf, red, True, tri_points, 5)

tri_pos = 100, 100

while 1:
    # "I wake to sleep, and take my waking slow"
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # "Regret shall be the gravel underfoot"
    screen.fill(bg)

    food = pygame.draw.circle(screen, cyan, (300, 300), 10, 2)
    blitted_rect = screen.blit(tri_surf, tri_pos)
    old_center = blitted_rect.center

    center_dot = pygame.draw.circle(screen, cyan, (old_center), 2, 1)

    tri_surf_rotated = pygame.transform.rotate(tri_surf, degree)
    rot_rect = tri_surf_rotated.get_rect()
    rot_rect.center = old_center

    tri = pygame.draw.polygon(tri_surf, red, tri_points, 2)
    screen.blit(tri_surf_rotated, rot_rect)

    # Increment rotation angle
    degree += 5
    if degree > 360:
        degree = 5

    #tri = tri.move(speed)

    pygame.display.flip()
    pygame.time.wait(60)

    '''
    TODO:
    write methods of creature class:
        __init__(self):
            self.vector = some vector heading
            self.last_sniff = strength of last collected food smell

        twiddle(self)
            rotate some random amount and stop on new heading

        travel(self, dist)
            move a set distance

        sniff(self)
            test concentration of "food smell"

     Run-loop logic will be as follows:  

        sniff() to establish initial food smell strength
        travel(some distance/time)
        (stop and) sniff() again

        if food smell strength has increased (or stayed the same?):
            carry on (repeat above steps)
        elif food smell strength has decreased:
            twiddle, and repeat steps
    '''


# References:
# Rotating an object about its center:
#     http://blog.tankorsmash.com/?p=128

