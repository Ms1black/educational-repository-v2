import sys
import os
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QCheckBox, QSlider, QScrollArea, QFrame, QGraphicsDropShadowEffect,
    QGridLayout
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor, QPen, QPainter, QBrush, QFontDatabase
from PyQt5.QtChart import QChart, QChartView, QLineSeries, QValueAxis

QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

STYLESHEET = """
QWidget#MainWindow { background-color: #f8f9fa; }
QWidget#ScrollContent { background-color: #f8f9fa; }
QWidget {
    font-family: 'Yandex Sans Text', Arial, sans-serif;
}
QLabel#WindowTitle {
    font-size: 20pt;
    font-weight: bold;
    color: #212529;
}
QFrame.Card {
    background-color: #ffffff;
    border-radius: 20px;
    border: none;
}
QLabel.CardTitle {
    font-size: 14pt;
    font-weight: bold;
    color: #212529;
}
QLabel.CardIcon {
    font-size: 16pt;
    color: #212529;
    padding-right: 8px;
}
QCheckBox {
    spacing: 12px;
    font-size: 12pt;
    color: #212529;
}
QCheckBox::indicator {
    width: 20px; height: 20px;
    border: 2px solid #dee2e6;
    border-radius: 6px;
    background-color: #f8f9fa;
}
QCheckBox::indicator:hover { border-color: #ffc107; }
QCheckBox::indicator:checked {
    background-color: #ffc107;
    border-color: #ffc107;
}
QSlider::groove:horizontal {
    border: 1px solid #dee2e6;
    background: #e9ecef;
    height: 8px;
    border-radius: 4px;
}
QSlider::handle:horizontal {
    background: #ffc107;
    border: 2px solid #ffffff;
    width: 20px; height: 20px;
    margin: -7px 0;
    border-radius: 11px;
}
QScrollArea { border: none; }
QScrollBar:vertical {
    border: none;
    background: #f8f9fa;
    width: 10px; margin: 0;
}
QScrollBar::handle:vertical {
    background-color: #dee2e6;
    min-height: 30px;
    border-radius: 5px;
}
QScrollBar::handle:vertical:hover { background-color: #ffc107; }
QToolTip {
    background-color: #212529;
    color: #ffffff;
    border: 1px solid #343a40;
    padding: 8px;
    border-radius: 6px;
    font-size: 10pt;
}
"""

class Card(QFrame):
    """Кастомный, переиспользуемый виджет, стилизованный под "карточку".

    Этот виджет представляет собой QFrame с закругленными углами, тенью для
    создания эффекта глубины, заголовком, иконкой и областью для
    размещения контента. Он служит для визуальной группировки элементов
    интерфейса.

    Args:
        title (str): Текст заголовка карточки.
        icon (str, optional): Unicode-символ для иконки.
        parent (QWidget, optional): Родительский виджет.
    """
    def __init__(self, title, icon=None, parent=None):
        super().__init__(parent)
        self.setProperty("class", "Card")

        shadow = QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(30)
        shadow.setColor(QColor(0, 0, 0, 40))
        shadow.setOffset(0, 5)
        self.setGraphicsEffect(shadow)

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(25, 20, 25, 20)
        self.main_layout.setSpacing(15)

        title_layout = QHBoxLayout()
        if icon:
            self.icon_label = QLabel(icon)
            self.icon_label.setProperty("class", "CardIcon")
            title_layout.addWidget(self.icon_label)
        
        self.title_label = QLabel(title)
        self.title_label.setProperty("class", "CardTitle")
        title_layout.addWidget(self.title_label)
        title_layout.addStretch()
        self.main_layout.addLayout(title_layout)
        
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setStyleSheet("color: #e9ecef;")
        self.main_layout.addWidget(separator)
        
        self.content_widget = QWidget()
        self.content_layout = QVBoxLayout(self.content_widget)
        self.content_layout.setContentsMargins(0, 5, 0, 5)
        self.main_layout.addWidget(self.content_widget)

class MainWindow(QMainWindow):
    """Главное окно приложения, которое собирает и отображает все элементы UI.

    Отвечает за общую компоновку, создание области прокрутки и инициализацию
    основных виджетов-карточек для графика и элементов управления.
    """
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.setWindowTitle("Домашнее задание №1")
        self.setGeometry(100, 100, 600, 850)
        self.setMinimumSize(550, 700)
        self._setup_ui()

    def _setup_ui(self):
        """Инициализирует и компонует все виджеты в главном окне."""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(15, 15, 15, 15)
        
        window_title = QLabel("Панель управления")
        window_title.setObjectName("WindowTitle")
        main_layout.addWidget(window_title, alignment=Qt.AlignCenter)
        main_layout.addSpacing(10)
        
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_content = QWidget()
        scroll_content.setObjectName("ScrollContent")
        
        self.scroll_layout = QVBoxLayout(scroll_content)
        self.scroll_layout.setContentsMargins(10, 10, 10, 10)
        self.scroll_layout.setSpacing(25)
        scroll_area.setWidget(scroll_content)
        main_layout.addWidget(scroll_area)

        self._create_graph_card()
        self._create_controls_card()
        self.scroll_layout.addStretch()

    def _create_graph_card(self):
        """Создает и добавляет в layout карточку с графиком функции."""
        graph_card = Card("График функции", icon="📈")
        self.chart_view = QChartView()
        self.chart_view.setMinimumHeight(300)
        self.chart_view.setRenderHint(QPainter.Antialiasing)
        self.plot_function_qtchart()
        graph_card.content_layout.addWidget(self.chart_view)
        self.scroll_layout.addWidget(graph_card)

    def _create_controls_card(self):
        """Создает и добавляет в layout карточку с интерактивными элементами."""
        controls_card = Card("Управление цветами")
        
        interactive_layout = QHBoxLayout()

        checkbox_container = QWidget()
        checkbox_layout = QVBoxLayout(checkbox_container)
        checkbox_layout.setContentsMargins(0,0,0,0)
        checkbox_layout.setSpacing(15)
        checkbox_container.setToolTip(
            "Установите флажки, чтобы отобразить или скрыть "
            "круги соответствующих цветов радуги."
        )

        circles_container = QWidget()
        self.circles_layout = QGridLayout(circles_container)
        self.circles_layout.setSpacing(15)

        interactive_layout.addWidget(checkbox_container, 1)
        interactive_layout.addWidget(circles_container, 2)
        controls_card.content_layout.addLayout(interactive_layout)

        self.checkboxes = []
        self.color_circles = []
        colors = {
            "Красный": "#d62828", "Оранжевый": "#f77f00", "Желтый": "#fcbf49",
            "Зеленый": "#8ac926", "Голубой": "#00b4d8", "Синий": "#0077b6", 
            "Фиолетовый": "#6a00f4"
        }
        
        for i, (name, code) in enumerate(colors.items()):
            checkbox = QCheckBox(name)
            checkbox.toggled.connect(self._update_controls_and_circles)
            self.checkboxes.append(checkbox)
            checkbox_layout.addWidget(checkbox)

            circle = QFrame()
            circle.setFixedSize(50, 50)
            circle.setStyleSheet(f"background-color: {code}; border-radius: 25px;")
            circle.setVisible(False)
            self.color_circles.append(circle)
            self.circles_layout.addWidget(circle, i // 4, i % 4, Qt.AlignCenter)
        
        checkbox_layout.addStretch()
        
        controls_card.content_layout.addSpacing(20)
        
        slider_layout = QHBoxLayout()
        slider_label = QLabel("Выбрано:")
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, len(colors))
        self.slider.setEnabled(False)
        self.count_label = QLabel("0")
        self.count_label.setFont(QFont("Yandex Sans Text", 12, QFont.Bold))
        slider_layout.addWidget(slider_label)
        slider_layout.addWidget(self.slider)
        slider_layout.addWidget(self.count_label)
        controls_card.content_layout.addLayout(slider_layout)

        self.scroll_layout.addWidget(controls_card)

    def plot_function_qtchart(self):
        """Вычисляет точки и строит график заданной функции на виджете QChartView."""
        series = QLineSeries()
        x_values = np.linspace(-2 * np.pi, 2 * np.pi, 2000)
        for x in x_values:
            if abs(np.cos(x**3)) < 1e-3: continue
            y = (1 - 10 * x - (x**2) / 13) * np.tan(x**3)
            if -100 < y < 100: series.append(x, y)

        chart = QChart()
        chart.addSeries(series)
        chart.setBackgroundBrush(QColor("transparent"))
        chart.legend().hide()
        chart.layout().setContentsMargins(0, 0, 0, 0)

        axis_pen = QPen(QColor("#dee2e6"))
        axis_brush = QBrush(QColor("#212529"))
        
        axis_x = QValueAxis()
        axis_x.setLinePen(axis_pen)
        axis_x.setLabelsBrush(axis_brush)
        chart.addAxis(axis_x, Qt.AlignBottom)
        series.attachAxis(axis_x)

        axis_y = QValueAxis()
        axis_y.setRange(-100, 100)
        axis_y.setLinePen(axis_pen)
        axis_y.setLabelsBrush(axis_brush)
        chart.addAxis(axis_y, Qt.AlignLeft)
        series.attachAxis(axis_y)

        series_pen = QPen(QColor("#212529"))
        series_pen.setWidth(3)
        series.setPen(series_pen)
        
        self.chart_view.setChart(chart)

    def _update_controls_and_circles(self):
        """Слот, который обновляет UI при изменении состояния чекбокса.

        Проходит по всем чекбоксам, обновляет видимость соответствующего
        цветного круга и пересчитывает значение для слайдера и счетчика.
        """
        checked_count = 0
        for i, checkbox in enumerate(self.checkboxes):
            is_checked = checkbox.isChecked()
            self.color_circles[i].setVisible(is_checked)
            if is_checked:
                checked_count += 1
        
        self.slider.setValue(checked_count)
        self.count_label.setText(str(checked_count))

if __name__ == '__main__':
    app = QApplication(sys.argv)

    font_dir = os.path.join(os.path.dirname(__file__), 'fonts')
    
    regular_font_id = QFontDatabase.addApplicationFont(
        os.path.join(font_dir, "YandexSansText-Regular.ttf")
    )
    bold_font_id = QFontDatabase.addApplicationFont(
        os.path.join(font_dir, "YandexSansText-Bold.ttf")
    )
    
    if regular_font_id != -1 and bold_font_id != -1:
        font_families = QFontDatabase.applicationFontFamilies(regular_font_id)
        if font_families:
            font_name = font_families[0]
            print(f"Шрифт '{font_name}' успешно загружен.")
    else:
        print("Ошибка: Не удалось загрузить кастомный шрифт.")

    app.setStyleSheet(STYLESHEET)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())