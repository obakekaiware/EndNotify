import sys

sys.path.append("../")

from main import execute


def test_create_message() -> None:
    command = "python sample.py"
    error_message = ""
    notification_message = create_message(command, error_message)
    ground_truth = "プログラムが問題なく終了しました。\n" "実行コマンド：\n" f"{command}"
    assert notification_message == ground_truth

    command = "python sample.py"
    error_message = "error message"
    notification_message = create_message(command, error_message)
    ground_truth = (
        "エラーが発生しました。\n" "実行コマンド：\n" f"{command}\n" "エラー内容：\n" f"{error_message}"
    )
    assert notification_message == ground_truth
