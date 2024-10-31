from PySide6.QtWidgets import QApplication, QWidget

# 명령줄 인수에 접근하기 위해서만 필요합니다.
import sys

# 애플리케이션당 하나(그리고 오직 하나)의 QApplication 인스턴스가 필요합니다.
# sys.argv를 전달하여 애플리케이션의 명령줄 인수를 허용합니다.
# 명령줄 인수를 사용하지 않을 것이라면 QApplication([])도 작동합니다.
app = QApplication(sys.argv)

# Qt 위젯을 생성합니다. 이 위젯이 우리의 창이 될 것입니다.
window = QWidget()
window.show()  # 중요!!!!! 창은 기본적으로 숨겨져 있습니다.

# 이벤트 루프를 시작합니다.
app.exec()

# 애플리케이션은 여기까지 도달하지 않으며, 종료하고 이벤트
# 루프가 중지될 때까지 기다립니다.
