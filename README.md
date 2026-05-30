<p align="center">
  <img src="https://github.com/koi-7/bcor-scheduler/assets/61448492/75783dcb-23d7-4a2a-9b03-b6c40424e51f">
</p>

# bcor-scheduler

公式サイトから来月の試合予定を読み取り、Google カレンダーに登録する

# Usage

## 0. 前提

uv を使用する

## 1. ダウンロード

``` bash
$ cd ~
$ git clone github:koi-7/bcor-scheduler.git
```

## 2. `bcor-scheduler/data/credentials.json` および `bcor-scheduler/config/config.ini` の準備

### `bcor-scheduler/data/credentials.json`

Google の credentials ファイルを用意する（サービスアカウント設定時にできる json ファイルの名前を `credenials.json` に変更して設置）

### `bcor-scheduler/.env`

`bcor-scheduler/.env_template` を参考に以下が書き込まれた `bcor-scheduler/config/.env` を作成する
- Google カレンダーのカレンダー ID
- Slack のチャンネル URL とトークン

## 3. `/opt/` に配置

``` bash
$ sudo mv ~/bcor-scheduler/ /opt/
```

## 4. 必要なパッケージをインストール

``` bash
$ uv sync
```

## 5-1. 実行例（通常）

``` bash
$ cd /opt/bcor-scheduler/
$ uv run -m bcor_scheduler
```

## 5-2. 実行例（cron で実行）

設定例: 毎月 15 日の 12 時に動くように cron を設定する

``` bash
$ crontab -e
```

```
CRON_TZ=Asia/Tokyo
PATH=$PATH:/home/<user name>/.local/bin/
0 12 15 * * cd /opt/bcor-scheduler/; uv run -m bcor_scheduler
```

タイムゾーンを反映するために cron を再起動する

``` bash
$ sudo systemctl restart cron
```
