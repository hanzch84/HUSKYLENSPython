import pygame, sys
from huskylib import HuskyLensLibrary

def main():
    # HuskyLens 초기화
    huskyLens = HuskyLensLibrary("I2C", "", address=0x32)
    huskyLens.algorthim("ALGORITHM_FACE_RECOGNITION")

    # pygame 초기화
    pygame.init()
    size = (800, 600)
    screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

    font = pygame.font.Font(None, 144)
    alpha = 0
    increasing = True

    running = True  # 프로그램 실행 여부를 나타내는 변수

    while running:  # 실행 중일 때만 루프를 돕니다.
        text = ""
        try:
            # 얼굴 데이터 가져오기
            faces = huskyLens.blocks()

            # 메시지 설정
            if faces and len(faces) > 0:
                for face in faces:
                    if face.learned:
                        text = f"Hello {face.ID}! How are you?"
                    else:
                        text = "Hello New Face!"
            else:
                text = "No face detected."
        except IndexError:
            print("데이터 처리 중 오류 발생: 인덱스 범위 초과")
        except Exception as e:
            print(f"알 수 없는 오류 발생: {e}")

        text_surface = font.render(text, True, (255, 255, 255))
        text_surface.set_alpha(alpha)

        # pygame 이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # 창을 닫으면 프로그램 종료
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:  # 'q' 키를 누르면 프로그램 종료
                    running = False

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

    pygame.quit()  # 루프가 종료되면 pygame을 종료합니다.
    sys.exit()

if __name__ == "__main__":
    main()
