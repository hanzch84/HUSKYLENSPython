import pygame, sys
from huskylib import HuskyLensLibrary

def main():
    # HuskyLens 초기화
    huskyLens = HuskyLensLibrary("I2C", "", address=0x32)
    huskyLens.algorthim("ALGORITHM_FACE_RECOGNITION")

    # pygame 초기화
    pygame.init()
    size = (1300, 700)
    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

    font = pygame.font.Font(None, 144)
    alpha = 0
    increasing = True

    while True:
        # 얼굴 데이터 가져오기
        faces = huskyLens.blocks()

        # 메시지 설정
        if faces:
            for face in faces:
                if face.learned:
                    text = f"Hello {face.ID}! How are you?"
                else:
                    text = "Hello New Face!"
        else:
            text = "No face detected."

        text_surface = font.render(text, True, (255, 255, 255))
        text_surface.set_alpha(alpha)

        # pygame 이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))
        
        # 알파값 조정
        if increasing:
            alpha += 1
            if alpha >= 255:
                increasing = False
        else:
            alpha -= 1
            if alpha <= 0:
                increasing = True

        text_surface.set_alpha(alpha)
        screen.blit(text_surface, (10, 250))

        pygame.display.update()
        pygame.time.delay(10)

if __name__ == "__main__":
    main()
