import cv2
import mediapipe as mp

# 初始化 MediaPipe 手部模型
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

# 定义手指索引
finger_tips = [8, 12, 16, 20]  # 食指、中指、无名指、小指的指尖
thumb_tip = 4  # 大拇指的指尖


def detect_finger_positions(landmarks):
    finger_status = []
    for tip in finger_tips:
        finger_status.append(landmarks[tip].y < landmarks[tip - 2].y)  # 比较指尖和指关节的y坐标
    thumb_status = landmarks[thumb_tip].x > landmarks[thumb_tip - 2].x  # 比较大拇指指尖和指关节的x坐标
    finger_status.append(thumb_status)
    return finger_status


def recognize_gesture(finger_status):
    # 识别0-9手势
    if not any(finger_status):
        return 0  # 全部手指收拢
    elif finger_status == [True, False, False, False, False]:
        return 1  # 食指伸出
    elif finger_status == [True, True, False, False, False]:
        return 2  # 食指和中指伸出
    elif finger_status == [True, True, True, False, False]:
        return 3  # 食指、中指和无名指伸出
    elif finger_status == [True, True, True, True, False]:
        return 4  # 四指伸出
    elif finger_status == [True, True, True, True, True]:
        return 5  # 全部手指伸出
    elif finger_status == [False, False, False, True, True]:
        return 6  # 大拇指和小指伸出
    elif finger_status == [True, False, False, False, True]:
        return 7  # 大拇指、食指和小指伸出
    elif finger_status == [True, True, False, False, True]:
        return 8  # 大拇指、食指和中指伸出
    elif finger_status == [True, True, True, False, True]:
        return 9  # 所有手指伸出，但小拇指收回
    else:
        return None  # 未识别手势


def hand_number(num_hands=1):
    # 初始化摄像头
    cap = cv2.VideoCapture(0)

    # 初始化 MediaPipe Hands 模块
    hands = mp_hands.Hands(static_image_mode=False, max_num_hands=num_hands, min_detection_confidence=0.7)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # 翻转视频帧，保证镜像模式
        frame = cv2.flip(frame, 1)

        # 将BGR图像转换为RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # 处理图像
        results = hands.process(rgb_frame)

        # 检测手部关键点
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # 在图像上绘制手部关键点和连接线
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # 解析每个手部关键点
                landmarks = hand_landmarks.landmark
                finger_status = detect_finger_positions(landmarks)
                gesture = recognize_gesture(finger_status)

                if gesture is not None:
                    cv2.putText(frame, f'Number: {gesture}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)

        # 显示图像
        cv2.imshow("Hand Number Recognition", frame)

        # 按下 'q' 键退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 释放资源
    cap.release()
    cv2.destroyAllWindows()
