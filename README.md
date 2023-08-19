# EndNotify

![EndNotify](https://github.com/obakekaiware/EndNotify/assets/49265616/2616b13a-043f-4e2f-9b99-88bf9ebdbe8f)

Python コードを実行し、終了したときに LINE で通知するツール。

実行途中でエラーが発生した場合、エラーメッセージを通知します。

## 1. 環境設定

「requirements.txt」を利用して必要なライブラリをインストールしてください。

```shell
pip install -r requirements.txt
```

「.env」を作成し、LINE Notify のトークンを登録してください。

```
LINE_NOTIFY_TOKEN = "Your Token"
```

## 2. 使い方

引数を実行コードとして、main 関数を起動します。

```shell
python main.py "python sample.py --a=1"
```

