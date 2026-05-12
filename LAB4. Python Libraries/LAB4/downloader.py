import sys
import threading
import time
import requests
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton,
    QProgressBar, QLabel, QMessageBox, QHBoxLayout
)
from PyQt5.QtCore import pyqtSignal, QObject
from matplotlib import pyplot as plt


class DownloaderSignals(QObject):
    progress = pyqtSignal(int, int)  # index, percent
    finished = pyqtSignal()


class Downloader(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Downloader")

        self.urls = [QLineEdit() for _ in range(3)]
        self.progress_bars = [QProgressBar() for _ in range(3)]
        self.percent_labels = [QLabel("0%") for _ in range(3)]
        self.download_times = [0, 0, 0]
        self.file_sizes = [0, 0, 0]
        self.threads = []

        self.signals = DownloaderSignals()
        self.signals.progress.connect(self.update_progress)
        self.signals.finished.connect(self.show_results)

        layout = QVBoxLayout()

        for i in range(3):
            layout.addWidget(QLabel(f"File URL {i+1}"))
            layout.addWidget(self.urls[i])

            h_layout = QHBoxLayout()
            h_layout.addWidget(self.progress_bars[i])
            h_layout.addWidget(self.percent_labels[i])
            layout.addLayout(h_layout)

        self.start_button = QPushButton("Start downloading!")
        self.start_button.clicked.connect(self.start_downloads)
        layout.addWidget(self.start_button)

        self.setLayout(layout)

    def start_downloads(self):
        # Сбрасываем предыдущие значения
        self.download_times = [0, 0, 0]
        self.file_sizes = [0, 0, 0]
        self.threads = []

        for i, url_edit in enumerate(self.urls):
            url = url_edit.text().strip()
            if url:
                t = threading.Thread(target=self.download_file, args=(i, url))
                t.start()
                self.threads.append(t)

        # поток для ожидания завершения всех загрузок
        threading.Thread(target=self.wait_for_completion).start()

    def download_file(self, index, url):
        start_time = time.time()
        try:
            r = requests.get(url, stream=True)
            r.raise_for_status()  # выброс исключения при HTTP ошибке

            total_length = r.headers.get('content-length')
            if total_length is None:
                total_length = 0
            else:
                total_length = int(total_length)
                self.file_sizes[index] = total_length

            filename = url.split("/")[-1] or f"file_{index+1}"
            downloaded = 0

            with open(filename, "wb") as f:
                for chunk in r.iter_content(chunk_size=4096):
                    if chunk:
                        f.write(chunk)
                        downloaded += len(chunk)
                        if total_length > 0:
                            percent = int(downloaded / total_length * 100)
                            self.signals.progress.emit(index, percent)

            self.download_times[index] = time.time() - start_time
            self.signals.progress.emit(index, 100)  # на всякий случай ставим 100%

        except Exception as e:
            self.signals.progress.emit(index, 0)
            self.percent_labels[index].setText("Error")
            print(f"Error downloading file {index+1}: {e}")

    def update_progress(self, index, percent):
        self.progress_bars[index].setValue(percent)
        self.percent_labels[index].setText(f"{percent}%")

    def wait_for_completion(self):
        for t in self.threads:
            t.join()
        self.signals.finished.emit()

    def show_results(self):
        # данные для графика
        times = [round(t, 3) for t in self.download_times if t > 0]
        sizes = [s / 1024 for s in self.file_sizes if s > 0]  # KB
        labels = [f"File {i+1}" for i, t in enumerate(self.download_times) if t > 0]

        if not times:
            QMessageBox.information(self, "Info", "Файлы не были скачаны")
            return

        # --- столбчатая диаграмма ---
        plt.figure(figsize=(8, 4))
        plt.bar(labels, times, color="skyblue")
        plt.title("Download time (s) vs File size (KB)")
        for i, t in enumerate(times):
            plt.text(i, t, f"{t:.3f}s\n{sizes[i]:.1f}KB", ha='center', va='bottom')
        plt.ylabel("Time (seconds)")
        plt.show()

        # --- круговая диаграмма ---
        plt.figure(figsize=(6, 6))
        plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140)
        plt.title("File size distribution (KB)")
        plt.show()


def run():
    app = QApplication(sys.argv)
    win = Downloader()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    run()