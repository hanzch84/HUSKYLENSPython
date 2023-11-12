import pygame
from huskylib import HuskyLensLibrary
import sys

# Pygame 초기화
pygame.init()

# 화면 크기 설정
screen_width = 1100
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))

students = {1:"MinKyoung", 2:"YoonSeo", 3:"HanNa", 4:"SiWon"}

# 폰트 설정
font = pygame.font.Font(None, 96)

# HuskyLens 객체를 생성합니다.
huskyLens = HuskyLensLibrary("I2C", "", address=0x32)

# 얼굴 인식 알고리즘 설정
huskyLens.algorthim("ALGORITHM_FACE_RECOGNITION")
sensortivity = 20
sensor = 0
while True:
    try:
        faces = huskyLens.blocks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if faces:
            # 반환된 값이 리스트인지 확인
            if not isinstance(faces, list):
                faces = [faces]  # 단일 객체를 리스트로 변환

            for face in faces:
                if face.learned:
                    text = f"Hello! {students[face.ID]}"
                else:
                    text = "Nice to meet you."
                
                # 화면을 검은색으로 채우고 텍스트를 그립니다.
                screen.fill((0, 0, 0))
                text_surface = font.render(text, True, (255, 255, 255))
                text_rect = text_surface.get_rect(center=(screen_width/2, screen_height/2))
                screen.blit(text_surface, text_rect)
                pygame.time.delay(1500)

                pygame.display.update()

        else:
            # 얼굴 데이터가 없을 경우 화면을 검은색으로 채우고 텍스트를 그립니다.
            screen.fill((0, 0, 0))
            text_surface = font.render("No face detected.", True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(screen_width/2, screen_height/2))
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
