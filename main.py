import os
import subprocess
import requests
import typer
from dotenv import load_dotenv


def execute(command: str) -> str:
    """コマンドを実行する関数

    Parameters
    ----------
    command : str
        実行したいコマンド。
        例: "python sample.py --a=1"

    Returns
    -------
    str
        command を実行した際のエラーメッセージ。
        エラーが発生せず実行終了したら、空文字列""が入る。
    """
    result = subprocess.run(command.split(), stderr=subprocess.PIPE)
    error_message = result.stderr.decode("utf-8")
    return error_message


def create_message(command: str, error_message: str) -> str:
    """通知メッセージを作成する関数

    Parameters
    ----------
    command : str
        実行したコマンド。
        例: "python sample.py --a=1"
    error_message : str
        command を実行したときのエラーメッセージ。

    Returns
    -------
    str
        通知メッセージ。
    """
    if error_message == "":
        notification_message = "プログラムが問題なく終了しました。\n" "実行コマンド：\n" f"{command}"
    else:
        notification_message = (
            "エラーが発生しました。\n" "実行コマンド：\n" f"{command}\n" "エラー内容：\n" f"{error_message}"
        )
    return notification_message


def notify(notification_message: str) -> None:
    """LINE Notify を使って通知メッセージを送る。

    Parameters
    ----------
    notification_message : str
        通知メッセージ。
    """
    load_dotenv(".env")
    line_notify_token = os.environ.get("LINE_NOTIFY_TOKEN")
    line_notify_api = "https://notify-api.line.me/api/notify"

    headers = {"Authorization": f"Bearer {line_notify_token}"}
    files = {"message": (None, notification_message)}
    requests.post(line_notify_api, headers=headers, files=files)


def main(command: str) -> None:
    """main関数

    Parameters
    ----------
    command : str
        Python の実行コード。
        ""で囲う必要がある。
        例: python main.py "python sample.py --a=1"
    """
    error_message = execute(command)
    notification_message = create_message(command, error_message)
    notify(notification_message)


if __name__ == "__main__":
    typer.run(main)
