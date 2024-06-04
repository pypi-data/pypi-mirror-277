import subprocess

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QFileDialog, QCompleter
from qfluentwidgets import PushButton, FlowLayout, ComboBox, SearchLineEdit

import ok.gui
from ok.capture.windows.dump import dump_threads
from ok.config.Config import Config
from ok.gui.widget.Tab import Tab
from ok.logging.Logger import get_logger
from ok.util.Handler import Handler

logger = get_logger(__name__)


class DebugTab(Tab):
    def __init__(self, app_config, exit_event):
        super().__init__()

        self.config = Config({'target_task': "", 'target_image': "", 'target_function': ""},
                             app_config.get('config_folder'), 'debug')
        tool_widget = QWidget()
        layout = FlowLayout(tool_widget, False)

        layout.setContentsMargins(0, 0, 0, 0)
        layout.setVerticalSpacing(20)
        layout.setHorizontalSpacing(10)
        self.handler = Handler(exit_event, "DebugTab")

        self.addCard(self.tr("Debug Tool"), tool_widget)

        dump_button = PushButton(self.tr("Dump Threads(HotKey:Ctrl+Alt+D)"))
        dump_button.clicked.connect(lambda: self.handler.post(dump_threads))
        layout.addWidget(dump_button)

        capture_button = PushButton(self.tr("Capture Screenshot"))
        capture_button.clicked.connect(lambda: self.handler.post(self.capture))
        layout.addWidget(capture_button)

        open_log_folder = PushButton(self.tr("Open Logs"))

        call_task_widget = QWidget()
        call_task_layout = FlowLayout(call_task_widget, False)
        self.addCard(self.tr("Debug Task Function"), call_task_widget)

        self.select_screenshot_button = PushButton(
            self.config.get('target_image') or self.tr("Drop or Select Screenshot"))
        self.select_screenshot_button.clicked.connect(self.select_screenshot)
        call_task_layout.addWidget(self.select_screenshot_button)

        self.tasks_combo_box = ComboBox()
        call_task_layout.addWidget(self.tasks_combo_box)
        tasks = ok.gui.executor.get_all_tasks()
        class_names = [obj.__class__.__name__ for obj in tasks]
        self.tasks_combo_box.addItems(class_names)
        self.tasks_combo_box.currentTextChanged.connect(self.task_changed)
        if self.config.get('target_task') in class_names:
            self.tasks_combo_box.setText(self.config.get('target_task'))
        else:
            self.tasks_combo_box.setCurrentIndex(0)

        target_function_edit = SearchLineEdit(self)
        target_function_edit.setPlaceholderText(self.tr('Type a stand name'))
        target_function_edit.setClearButtonEnabled(True)
        target_function_edit.setFixedWidth(230)
        stands = [
            "Star Platinum", "Hierophant Green",
            "Made in Haven", "King Crimson",
            "Silver Chariot", "Crazy diamond",
            "Metallica", "Another One Bites The Dust",
            "Heaven's Door", "Killer Queen",
            "The Grateful Dead", "Stone Free",
            "The World", "Sticky Fingers",
            "Ozone Baby", "Love Love Deluxe",
            "Hermit Purple", "Gold Experience",
            "King Nothing", "Paper Moon King",
            "Scary Monster", "Mandom",
            "20th Century Boy", "Tusk Act 4",
            "Ball Breaker", "Sex Pistols",
            "D4C • Love Train", "Born This Way",
            "SOFT & WET", "Paisley Park",
            "Wonder of U", "Walking Heart",
            "Cream Starter", "November Rain",
            "Smooth Operators", "The Matte Kudasai"
        ]
        self.completer = QCompleter(stands, target_function_edit)
        self.completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.completer.setMaxVisibleItems(10)
        target_function_edit.setCompleter(self.completer)

    def task_changed(self, text):
        self.config['target_task'] = text

    def select_screenshot(self):
        file_name, _ = QFileDialog.getOpenFileName(None, "Open Image", "", "Image Files (*.png *.jpg *.bmp)")

        if file_name:
            logger.info(f"Selected files: {file_name}")
            self.select_screenshot_button.setText(file_name)
            self.config['target_image'] = file_name
        else:
            self.select_screenshot_button.setText(self.tr("Drop or Select Screenshot"))
            self.config['target_image'] = None

    def capture(self):
        if ok.gui.device_manager.capture_method is not None:
            logger.info(f'ok.gui.device_manager.capture_method {ok.gui.device_manager.capture_method}')
            capture = str(ok.gui.device_manager.capture_method)
            frame = ok.gui.device_manager.capture_method.do_get_frame()
            if frame is not None:
                file_path = ok.gui.ok.screenshot.generate_screen_shot(frame, ok.gui.ok.screenshot.ui_dict,
                                                                      ok.gui.ok.screenshot.screenshot_folder, capture)

                # Use subprocess.Popen to open the file explorer and select the file
                subprocess.Popen(r'explorer /select,"{}"'.format(file_path))
                logger.info(f'captured screenshot: {capture}')
                self.alert_info(self.tr('Capture Success'))
            else:
                self.alert_error(self.tr('Capture returned None'))
        else:
            self.alert_error(self.tr('No Capture Available or Selected'))
