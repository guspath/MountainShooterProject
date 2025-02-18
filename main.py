import pygame

print('Setup Start')
pygame.init()
print('Setup Done')
window = pygame.display.set_mode(size=(800, 600))

print('Loop Start')
while True:
    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # Close Window
            quit()  # end pygame
