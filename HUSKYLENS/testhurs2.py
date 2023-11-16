import pygame
from huskylib import HuskyLensLibrary
import sys
from math import pi

# Pygame 초기화
pygame.init()

# 화면 크기 설정
screen_width = 1920
screen_height = 1080
screen = pygame.display.set_mode((screen_width, screen_height),pygame.FULLSCREEN)

students = {1:"Min Kyoung", 2:"Yoon Seo", 3:"Han Na", 4:"Si Won"}

# 폰트 설정
font = pygame.font.Font(None, 288)

# HuskyLens 객체를 생성합니다.
huskyLens = HuskyLensLibrary("I2C", "", address=0x32)

# 얼굴 인식 알고리즘 설정
huskyLens.algorthim("ALGORITHM_FACE_RECOGNITION")
sensortivity = 20
sensor = 0
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
                    print(face.x,face.y)
                else:
                    text = "Nice to meet you."
                
                # 화면을 검은색으로 채우고 텍스트를 그립니다.
                screen.fill((0, 0, 0))
                text_surface = font.render(text, True, (255, 255, 255))
                text_rect = text_surface.get_rect(center=(screen_width/2, screen_height/2))
                screen.blit(text_surface, text_rect)
                
                pygame.draw.circle(screen,[255,255,255],[160,120],120)
                pygame.draw.circle(screen,[255,255,255],[160+320,120],120)

                pygame.draw.circle(screen,[11,0,0],[320-face.x,face.y],60)
                pygame.draw.circle(screen,[0,0,0],[320-face.x,face.y],10)
                pygame.draw.circle(screen,[11,0,0],[320-face.x+320,face.y],60)
                pygame.draw.circle(screen,[0,0,0],[320-face.x+320,face.y],10)
                pygame.draw.ellipse(screen,[205,205,205],[230,180,180,120])
                pygame.draw.arc(screen,[255,255,255], [80,200,500,200],pi,2*pi,15)
                pygame.time.delay(200)

                pygame.display.update()

        else:
            # 얼굴 데이터가 없을 경우 화면을 검은색으로 채우고 텍스트를 그립니다.
            screen.fill((0, 0, 0))
            text_surface = font.render("Anyone here?", True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(screen_width/2, screen_height/2))
            screen.blit(text_surface, text_rect)
            pygame.display.update()
    except IndexError:
            if sensor == sensortivity:
                    
                # 얼굴 데이터가 없을 경우 화면을 검은색으로 채우고 텍스트를 그립니다.
                screen.fill((0, 0, 0))
                text_surface = font.render("Anyone here?", True, (255, 255, 255))
                text_rect = text_surface.get_rect(center=(screen_width/2, screen_height/2))
                screen.blit(text_surface, text_rect)

                pygame.draw.circle(screen,[255,255,255],[160,120],120)
                pygame.draw.circle(screen,[255,255,255],[160+320,120],120)

                pygame.draw.circle(screen,[11,0,0],[160,120],60)
                pygame.draw.circle(screen,[0,0,0],[160,120],10)
                pygame.draw.circle(screen,[11,0,0],[160+320,120],60)
                pygame.draw.circle(screen,[0,0,0],[160+320,120],10)
                pygame.draw.ellipse(screen,[205,205,205],[230,180,180,120])
                pygame.draw.arc(screen,[255,255,255], [80,300,500,100],pi,2*pi,15)

                pygame.display.update()
                sensor = 0
            else:
                sensor += 1
                pygame.time.delay(20)

    except Exception as e:
        print(f"알 수 없는 오류 발생: {e}")
