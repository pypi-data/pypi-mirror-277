import cv2
from deepface import DeepFace
import time

class FineFace:
    def __init__(self):
        # 表情转换字典
        self.emotion_translation = {
            "angry": "生气",
            "disgust": "厌恶",
            "fear": "害怕",
            "happy": "高兴",
            "sad": "伤心",
            "surprise": "惊讶",
            "neutral": "中性"
        }

        # 加载预训练的人脸检测模型
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        # 打开摄像头
        self.cap = cv2.VideoCapture(0)  # 0表示默认摄像头

        # 检查摄像头是否成功打开
        if not self.cap.isOpened():
            print("无法打开摄像头")
            exit()

    def fine_emo(self):
        # 记录启动时的时间戳
        start_time = time.time()

        try:
            while True:
                # 读取视频流的帧
                ret, frame = self.cap.read()

                if not ret:
                    print("无法读取视频流")
                    break

                # 转换为灰度图像
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

                # 检测人脸
                faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

                # 获取当前时间
                current_time = time.time()

                # 每隔10秒进行一次表情识别
                if current_time - start_time > 10:
                    results = []
                    for (x, y, w, h) in faces:
                        # 提取人脸区域
                        face = frame[y:y+h, x:x+w]

                        # 使用DeepFace进行情绪识别，设置enforce_detection为False
                        try:
                            analysis = DeepFace.analyze(face, actions=['emotion'], enforce_detection=False)

                            # 获取情绪分析结果
                            if isinstance(analysis, list):
                                emotion = analysis[0]['dominant_emotion']
                            else:
                                emotion = analysis['dominant_emotion']

                            # 转换为中文表情
                            emotion_chinese = self.emotion_translation.get(emotion, "未知")

                            # 绘制矩形框并标注情绪
                            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                            cv2.putText(frame, emotion_chinese, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)

                            # 打印识别结果到控制台
                            print(f"识别到的表情: {emotion_chinese}")

                            # 保存识别结果
                            results.append({
                                "time": current_time,
                                "emotion": emotion_chinese,
                                "coordinates": (x, y, w, h)
                            })
                        except ValueError as e:
                            print(f"情绪分析失败: {e}")

                    # 重置时间戳
                    start_time = current_time

                    yield results

                # 显示结果
                cv2.imshow('Emotion Recognition', frame)

                # 按下 'q' 键退出循环
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        except KeyboardInterrupt:
            print("程序被中断")
        finally:
            # 释放摄像头并关闭窗口
            self.cap.release()
            cv2.destroyAllWindows()

if __name__ == '__main__':
    fine_face = FineFace()
    for recognition_results in fine_face.fine_emo():
        print("识别结果：", recognition_results)


