import pygame
from huskylib import HuskyLensLibrary
import sys

# Pygame 초기화
pygame.init()

# 화면 크기 설정
screen_width = 1280
screen_height = 768
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

students = {1: "Min Kyoung", 2: "Yoon Seo", 3: "Han Na", 4: "Si Won"}

# 폰트 설정
font = pygame.font.Font(None, 128)

# HuskyLens 객체를 생성합니다.
huskyLens = HuskyLensLibrary("I2C", "", address=0x32)

# 얼굴 인식 알고리즘 설정
huskyLens.algorthim("ALGORITHM_FACE_RECOGNITION")
sensortivity = 20
sensor = 0

# 텍스트와 알파값을 관리할 변수 추가
text = ""
alpha = 0  # 초기 알파값

while True:
    try:
        # 이벤트 루프를 사용하여 키보드 입력 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # 'q' 키를 누르면 프로그램 종료
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

        # 마우스 포인터 숨기기
        pygame.mouse.set_visible(False)

        faces = huskyLens.blocks()

        if faces:
            # 반환된 값이 리스트인지 확인
            if not isinstance(faces, list):
                faces = [faces]  # 단일 객체를 리스트로 변환

            for face in faces:
                if face.learned:
                    # 얼굴을 인식하면 "Hello! Name" 텍스트를 설정
                    text = f"Hello! {students[face.ID]}"

                # 알파값을 부드럽게 증가시킴
                if alpha < 255:
                    alpha += 5

                # 화면을 검은색으로 채우고 텍스트와 알파값을 사용하여 부드럽게 표시
                screen.fill((0, 0, 0))
                text_surface = font.render(text, True, (255, 255, 255, alpha))
                text_rect = text_surface.get_rect(center=(screen_width / 2, screen_height / 2))
                screen.blit(text_surface, text_rect)

                pygame.display.update()
        else:
            # 얼굴 데이터가 없을 경우 텍스트를 초기화하고 알파값을 다시 0으로 설정하여 사라지게 함
            text = "Nice to Meet you!"

            # 알파값을 부드럽게 감소시킴
            if alpha > 0:
                alpha -= 5

            # 화면을 검은색으로 채우고 텍스트와 알파값을 사용하여 부드럽게 표시
            screen.fill((0, 0, 0))
            text_surface = font.render(text, True, (255, 255, 255, alpha))
            text_rect = text_surface.get_rect(center=(screen_width / 2, screen_height / 2))
            screen.blit(text_surface, text_rect)

            pygame.display.update()
    except IndexError:
            if sensor == sensortivity:
                    
                # 얼굴 데이터가 없을 경우 화면을 검은색으로 채우고 텍스트를 그립니다.
                screen.fill((0, 0, 0))
                text_surface = font.render("No face detected.", True, (255, 255, 255))
                text_rect = text_surface.get_rect(center=(screen_width/2, screen_height/2))
                screen.blit(text_surface, text_rect)
                pygame.display.update()
                sensor = 0
            else:
                sensor += 1
                pygame.time.delay(20)

    except Exception as e:
        print(f"알 수 없는 오류 발생: {e}")
