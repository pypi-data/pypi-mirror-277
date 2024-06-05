import cv2
from deepface import DeepFace

class FineFace:
    def __init__(self):
        # 加载预训练的Haar特征分类器模型
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarWcascade_eye.xml')
        self.smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')
        # 打开摄像头
        self.cap = cv2.VideoCapture(0)

    def face(self):
        """检测人脸、眼睛和笑容"""
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                roi_gray = gray[y:y + h, x:x + w]
                roi_color = frame[y:y + h, x:x + w]

                eyes = self.eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=10, minSize=(15, 15))
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

                smiles = self.smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.8, minNeighbors=20, minSize=(25, 25))
                for (sx, sy, sw, sh) in smiles:
                    cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (0, 0, 255), 2)

            cv2.imshow('人脸检测', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

    def analyze_age(self):
        """检测并显示年龄"""
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            result = DeepFace.analyze(frame, actions=['age'])

            if 'age' in result:
                age = result['age']
                cv2.putText(frame, f'年龄: {age}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            cv2.imshow('年龄检测', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

    def analyze_gender(self):
        """检测并显示性别"""
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            result = DeepFace.analyze(frame, actions=['gender'])

            if 'gender' in result:
                gender = result['gender']
                cv2.putText(frame, f'性别: {gender}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            cv2.imshow('性别检测', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

    def analyze_emotion(self):
        """检测并显示情绪"""
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            result = DeepFace.analyze(frame, actions=['emotion'])

            if 'dominant_emotion' in result:
                emotion = result['dominant_emotion']
                cv2.putText(frame, f'情绪: {emotion}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            cv2.imshow('情绪检测', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    fine_face = FineFace()
    mode = input("输入 'f' 进行基础人脸检测，'a' 进行年龄检测，'g' 进行性别检测，或 'e' 进行情绪检测: ").strip().lower()
    if mode == 'f':
        fine_face.face()
    elif mode == 'a':
        fine_face.analyze_age()
    elif mode == 'g':
        fine_face.analyze_gender()
    elif mode == 'e':
        fine_face.analyze_emotion()
