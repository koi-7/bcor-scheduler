<p align="center">
  <img src="https://github.com/koi-7/bcor-scheduler/assets/61448492/75783dcb-23d7-4a2a-9b03-b6c40424e51f">
</p>

# bcor-scheduler

公式サイトから来月の試合予定を読み取り、Google カレンダーに登録する

# Usage

## 1. ダウンロード

``` bash
$ cd ~
$ git clone github:koi-7/bcor-scheduler.git
```

## 2. `bcor-scheduler/data/credentials.json` および `bcor-scheduler/config/config.ini` の準備

### `bcor-scheduler/data/credentials.json`

Google の credentials ファイルを用意する（サービスアカウント設定時にできる json ファイルの名前を `credenials.json` に変更して設置）

### `bcor-scheduler/config/config.ini`

`bcor-scheduler/config/template.ini` を参考に以下が書き込まれた `bcor-scheduler/config/config.ini` を作成する
- Google カレンダーのカレンダー ID
- Slack のチャンネル URL とトークン

## 3. Requirements

``` bash
$ pip3 install -r bcor-scheduler/requirements.txt
```

## 4. `/opt/` に配置

``` bash
$ sudo mv bcor-scheduler/ /opt/
```

## 5. `~/.bashrc` に PYTHONPATH を設定

``` bash
$ vim ~/.bashrc
```

```
export PYTHONPATH=$PYTHONPATH:/opt/bcor-scheduler/
```

設定を反映させる

``` bash
$ source ~/.bashrc
```

## 6. cron の設定（例）

毎月 15 日の 12 時に動くように cron を設定する

``` bash
$ crontab -e
```

```
CRON_TZ=Asia/Tokyo
0 12 15 * * /usr/bin/python3 -m bcor-scheduler
```

タイムゾーンを反映するために cron を再起動する

``` bash
$ sudo systemctl restart cron
```
