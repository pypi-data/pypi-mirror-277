import subprocess

from PySide6.QtWidgets import QWidget, QFileDialog
from qfluentwidgets import PushButton, FlowLayout, ComboBox

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

        self.config = Config({'target_task': None, 'target_image': None, 'target_function': None},
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

        select_screenshot = PushButton(self.tr("Drop or Select Screenshot"))
        select_screenshot.clicked.connect(lambda: self.handler.post(self.select_screenshot))
        call_task_layout.addWidget(select_screenshot)

        self.tasks_combo_box = ComboBox()
        call_task_layout.addWidget(self.tasks_combo_box)
        tasks = ok.gui.executor.get_all_tasks()
        class_names = [obj.__class__.__name__ for obj in tasks]
        self.tasks_combo_box.addItems(class_names)
        if self.config.get('target_task') in class_names:
            self.tasks_combo_box.setText(self.config.get('target_task'))
        else:
            self.tasks_combo_box.setCurrentIndex(0)

    def select_screenshot(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.ExistingFiles)

        if dialog.exec_() == QFileDialog.Accepted:
            selected_files = dialog.selectedFiles()
            logger.info(f"Selected files: {selected_files}")

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
