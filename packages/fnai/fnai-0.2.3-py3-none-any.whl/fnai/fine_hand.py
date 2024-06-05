import cv2
import mediapipe as mp

def hand_gesture_recognition():
    # 初始化 MediaPipe 手部模型
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.7)
    mp_draw = mp.solutions.drawing_utils

    # 打开摄像头
    cap = cv2.VideoCapture(0)

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
                h, w, c = frame.shape
                finger_status = []
                for idx in range(0, 21, 4):
                    landmark = hand_landmarks.landmark[idx]
                    cx, cy = int(landmark.x * w), int(landmark.y * h)
                    finger_status.append((cx, cy))

                number = recognize_number(finger_status)
                cv2.putText(frame, f'Number: {number}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)

        # 显示图像
        cv2.imshow("Hand Gesture Recognition", frame)

        # 按下 'q' 键退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 释放资源
    cap.release()
    cv2.destroyAllWindows()

def recognize_number(finger_status):
    thumb_tip = finger_status[1]
    index_tip = finger_status[2]
    middle_tip = finger_status[3]
    ring_tip = finger_status[4]
    pinky_tip = finger_status[5]

    thumb_up = thumb_tip[1] < finger_status[0][1]
    index_up = index_tip[1] < finger_status[0][1]
    middle_up = middle_tip[1] < finger_status[0][1]
    ring_up = ring_tip[1] < finger_status[0][1]
    pinky_up = pinky_tip[1] < finger_status[0][1]

    if thumb_up and not index_up and not middle_up and not ring_up and not pinky_up:
        return 1
    elif thumb_up and index_up and not middle_up and not ring_up and not pinky_up:
        return 2
    elif thumb_up and index_up and middle_up and not ring_up and not pinky_up:
        return 3
    elif thumb_up and index_up and middle_up and ring_up and not pinky_up:
        return 4
    elif thumb_up and index_up and middle_up and ring_up and pinky_up:
        return 5
    elif not thumb_up and index_up and middle_up and ring_up and pinky_up:
        return 6
    elif not thumb_up and index_up and middle_up and ring_up and not pinky_up:
        return 7
    elif not thumb_up and index_up and middle_up and not ring_up and not pinky_up:
        return 8
    elif not thumb_up and index_up and not middle_up and not ring_up and not pinky_up:
        return 9
    else:
        return 0

