import serial
import serial.tools.list_ports
import time
import threading

class PyArduino:
    def __init__(self):
        """
        수신받은 데이터 값을 저장하는 변수 초기화
        메인 쓰레드 종료 여부 확인 변수 초기화
        아두이노 객체 초기화
        """
        self.serial_receive_data = ""
        self.main_thread_finished = False
        self.arduino = None  
        
    def connect(self):
        """
        ===========================================
        시리얼 클래스를 사용하여 아두이노 객체 생성
        
        직렬 포트를 검색하여 'Arduino Uno'가 포함된 포트를 찾아 연결합니다.
        
        예제:
        >>> py_arduino = PyArduino()
        >>> py_arduino.connect()
        (포트를 검색하여 아두이노를 연결합니다.)
        
        """
        ports = list(serial.tools.list_ports.comports())
        for p in ports:
            if "Arduino Uno" in p.description:
                print(f"{p} 포트에 연결하였습니다.")
                self.arduino = serial.Serial(p.device, baudrate=9600, timeout=1.0)
                time.sleep(2.0) 

    def close(self):
        """
        =====================
        시리얼 포트 연결 종료
        
        예제:
        >>> py_arduino = PyArduino()
        >>> py_arduino.connect()
        >>> py_arduino.close()
        (아두이노와의 연결을 종료합니다.)
        """
        if self.arduino:
            self.arduino.close()
            print("연결을 종료하였습니다.")
            
    def send_rgb(self, cnt=1):
        """ 
        =========================================================
        빨강, 초록, 파랑 순서로 매개변수 횟수만큼 RGB LED 깜빡이기
        
        매개변수:
        - cnt (int): LED를 깜빡일 횟수
        
        예제:
        >>> py_arduino = PyArduino()
        >>> py_arduino.connect()
        >>> py_arduino.send_rgb(3)
        (RGB LED를 빨강, 초록, 파랑 순서로 3회 깜빡입니다.)
        """
        self.cnt = cnt
        for i in range(self.cnt):
            self.arduino.write("RGB=255,0,0\n".encode())
            time.sleep(1)
            self.arduino.write("RGB=0,255,0\n".encode())
            time.sleep(1)
            self.arduino.write("RGB=0,0,255\n".encode())
            time.sleep(1)
        self.arduino.write("RGB=0,0,0\n".encode())  # LED 끄고 종료
    
    # 매개변수로 RGB값 받아서 색만들어 LED켜기
    def send_rgb_color(self, red=255, green=255, blue=255):
        """
        ===================================
        매개변수로 받은 RGB 값으로 LED 켜기

        매개변수:
        - red (int): 빨강 값 (0~255)
        - green (int): 초록 값 (0~255)
        - blue (int): 파랑 값 (0~255)

        예제:
        >>> py_arduino = PyArduino()
        >>> py_arduino.connect()
        >>> py_arduino.send_rgb_color(255, 100, 50)
        (RGB LED를 빨강 255, 초록 100, 파랑 50으로 설정하여 켭니다.)
        """
        self.arduino.write(f'RGB={red},{green},{blue}\n'.encode())
            
    def send_servo(self,digree):
        """
        =========================
        서보모터 각도 데이터 전송
        
        매개변수:
        - degree (int): 서보모터 각도 (0~180)
        
        예제:
        >>> py_arduino = PyArduino()
        >>> py_arduino.connect()
        >>> py_arduino.send_servo(90)
        (서보모터를 90도로 회전시킵니다.)
        """
        self.arduino.write(f"SERVO={digree}\n".encode())
        
    def send_buzzer(self,freq):
        """
        ============================
        버저 음계 주파수 데이터 전송
        
        주어진 주파수를 아두이노로 전송하여 버저로 해당 음계를 재생합니다.
        
        매개변수:
        - freq (int): 전송할 음계의 주파수 (Hz)
        
        음계와 해당 주파수:
        - 도 (C4) : 261.63 Hz
        - 레 (D4) : 293.66 Hz
        - 미 (E4) : 329.63 Hz
        - 파 (F4) : 349.23 Hz
        - 솔 (G4) : 392.00 Hz
        - 라 (A4) : 440.00 Hz
        - 시 (B4) : 493.88 Hz
        - 높은 도 (C5) : 523.25 Hz
        
        예제:
        >>> py_arduino = PyArduino()
        >>> py_arduino.connect()
        >>> py_arduino.send_buzzer(440)
        (아두이노에 440 Hz의 라(A4) 음을 전송합니다.)
        """          
        self.arduino.write(f"BUZZER={freq}\n".encode())
        
    def send_fnd(self,data):
        """
        ======================================
        FND (7세그먼트 디스플레이) 데이터 전송
        
        매개변수:
        - data (str): FND에 표시할 데이터
        
        예제:
        >>> py_arduino = PyArduino()
        >>> py_arduino.connect()
        >>> py_arduino.send_fnd("1234")
        (FND에 '1234'를 표시합니다.)
        """
        self.arduino.write(f"FND={data}\n".encode()) 
        
    def send_vr(self):
        """
        =====================
        VR (가변저항) 값 요청
        
        예제:
        >>> py_arduino = PyArduino()
        >>> py_arduino.connect()
        >>> py_arduino.send_vr()
        (가변저항 값을 요청합니다.)
        """
        self.arduino.write("VR=?\n".encode())
    
    def send_bright(self):
        """
        =================
        조도 센서 값 요청
        
        예제:
        >>> py_arduino = PyArduino()
        >>> py_arduino.connect()
        >>> py_arduino.send_bright()
        (조도 센서 값을 요청합니다.)
        """
        self.arduino.write("BRIGHT=?\n".encode())
        
    def send_temperature(self):
        """
        =================
        온도 센서 값 요청
        
        예제:
        >>> py_arduino = PyArduino()
        >>> py_arduino.connect()
        >>> py_arduino.send_temperature()
        (온도 센서 값을 요청합니다.)
        """
        self.arduino.write(f"TEMPERATURE=?\n".encode())

    def send_humidity(self):
        """
        =================
        습도 센서 값 요청
        
        예제:
        >>> py_arduino = PyArduino()
        >>> py_arduino.connect()
        >>> py_arduino.send_humidity()
        (습도 센서 값을 요청합니다.)
        """
        self.arduino.write(f"HUMIDITY=?\n".encode())

    def send_object_temperature(self):
        """
        ======================
        물체 온도 센서 값 요청
        
        예제:
        >>> py_arduino = PyArduino()
        >>> py_arduino.connect()
        >>> py_arduino.send_object_temperature()
        (물체 온도 센서 값을 요청합니다.)
        """
        self.arduino.write(f"OBJECT=?\n".encode())

    def send_ambient_temperature(self):
        """
        ======================
        주변 온도 센서 값 요청
        
        예제:
        >>> py_arduino = PyArduino()
        >>> py_arduino.connect()
        >>> py_arduino.send_ambient_temperature()
        (주변 온도 센서 값을 요청합니다.)
        """
        self.arduino.write(f"AMBIENT=?\n".encode())

        
    def serial_send_thread(self):
        """
        =========================================
        주기적으로 센서 값을 요청하는 쓰레드 함수
        send_thread() 함수 내부에서 호출
        
        예제:
        >>> py_arduino = PyArduino()
        >>> py_arduino.connect()
        >>> py_arduino.send_thread()
           (serial_send_thread 함수를 실행하는 쓰레드를 생성)
        """
        while True:
            self.send_vr()
            time.sleep(0.1)
            self.send_bright()
            time.sleep(0.1)
            self.send_temperature()
            time.sleep(0.1)
            self.send_humidity()
            time.sleep(0.1)
            self.send_object_temperature()
            time.sleep(0.1)
            self.send_ambient_temperature()
            time.sleep(0.1)
            if self.main_thread_finished:  
                break

    def serial_read_thread(self):
        """
        =========================================
        시리얼 포트에서 데이터를 읽는 쓰레드 함수
        read_thread() 함수 내부에서 호출
    
        예제:
        >>> py_arduino = PyArduino()
        >>> py_arduino.connect()
        >>> py_arduino.read_thread()
            (serial_read_thread 함수를 실행하는 쓰레드를 생성)
        """
        while True:
            read_data=self.arduino.readline()
            self.serial_receive_data = read_data.decode().strip()
            if self.main_thread_finished:  
                break
                   
    def send_thread(self):
        """
        ===============================
        센서 값 요청을 위한 쓰레드 시작
        
        예제:
        >>> py_arduino = PyArduino()
        >>> py_arduino.connect()
        >>> py_arduino.send_thread()
        (센서 값을 주기적으로 요청하는 쓰레드를 시작합니다.)
        """
        t1 = threading.Thread(target=self.serial_send_thread)
        t1.daemon = True
        t1.start()        
        
    def read_thread(self):
        """
        ==========================================
        시리얼 포트 데이터를 읽기 위한 쓰레드 시작
        
        예제:
        >>> py_arduino = PyArduino()
        >>> py_arduino.connect()
        >>> py_arduino.read_thread()
        (시리얼 포트 데이터를 읽는 쓰레드를 시작합니다.)
        """
        t2 = threading.Thread(target=self.serial_read_thread)
        t2.daemon = True
        t2.start()