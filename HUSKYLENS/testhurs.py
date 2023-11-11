from huskylib import HuskyLensLibrary

# HuskyLens 객체를 생성합니다.
huskyLens = HuskyLensLibrary("I2C", "", address=0x32)
 
# 얼굴 인식 알고리즘 설정
huskyLens.algorthim("ALGORITHM_FACE_RECOGNITION")

while True:
    try:
        faces = huskyLens.blocks()
        if faces:
            # 반환된 값이 리스트인지 확인
            if not isinstance(faces, list):
                faces = [faces]  # 단일 객체를 리스트로 변환

            for face in faces:
                if face.learned:
                    print(f"훈련된 얼굴 ID {face.ID}: 위치 ({face.x}, {face.y}), 크기 ({face.width}x{face.height})")
                else:
                    print(f"훈련되지 않은 얼굴: 위치 ({face.x}, {face.y}), 크기 ({face.width}x{face.height})")
        else:
            print("얼굴 데이터가 없습니다. ")
    except IndexError:
        print("데이터 처리 중 오류 발생: 인덱스 범위 초과")
    except Exception as e:
        print(f"알 수 없는 오류 발생: {e}")
