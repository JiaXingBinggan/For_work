import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QTextCursor, QFont
from PyQt5.QtCore import Qt
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

os.environ["CUDA_VISIBLE_DEVICES"] = '-1'
device = 'cuda' if torch.cuda.is_available() else 'cpu'

local_model_path = "Chinese_Chat_T5_Base"
tokenizer = AutoTokenizer.from_pretrained(local_model_path)
model = AutoModelForSeq2SeqLM.from_pretrained(local_model_path)
model.to(device)


def postprocess(text):
    return text.replace(".", "").replace('</>', '')


def answer_fn(text, top_k=50):
    encoding = tokenizer(text=[text], truncation=True, padding=True, max_length=256, return_tensors="pt").to(device)
    out = model.generate(**encoding, return_dict_in_generate=True, output_scores=False, max_length=512, temperature=0.5,
                         do_sample=True, repetition_penalty=3.0, top_k=top_k)
    result = tokenizer.batch_decode(out["sequences"], skip_special_tokens=True)
    return postprocess(result[0])


class ChatWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("聊天机器人")
        self.setGeometry(100, 100, 800, 600)

        font = QFont("Arial", 14)

        self.chat_history = QTextEdit(self)
        self.chat_history.setReadOnly(True)
        self.chat_history.setFont(font)

        self.input_box = QLineEdit(self)
        self.input_box.setFont(font)
        self.input_box.returnPressed.connect(self.send_message)

        self.send_button = QPushButton("发送", self)
        self.send_button.setFont(font)
        self.send_button.clicked.connect(self.send_message)

        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.chat_history)
        layout.addWidget(self.input_box)
        layout.addWidget(self.send_button)
        self.setCentralWidget(central_widget)

    def send_message(self):
        user_input = self.input_box.text()
        self.chat_history.append(f"<font color='blue'>用户: {user_input}</font>")
        self.input_box.clear()

        response = answer_fn(user_input, top_k=50)
        self.chat_history.append(f"<font color='green'>机器人: {response}</font>")

        self.chat_history.moveCursor(QTextCursor.End)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ChatWindow()
    window.show()
    sys.exit(app.exec_())