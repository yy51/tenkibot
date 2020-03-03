# Twitterで雨をお知らせするbot

## 何を作ったか
毎日2回，AM 0:30とAM 7:00にその日の天気予報を取得し，降水確率(0-6時，6-12時，12-18時，18-24時)がひとつでも30%を超えていれば「傘が必要です」とtweetするbot．

## なぜ作ったか
Twitterは見てるのに天気予報は見てなくて雨が降って困った，という自分の体験から，こういうbotがあれば雨対策ができると考えたから．

## デプロイ先
https://twitter.com/ten_ki_tashin

## 仕組み
pythonのコードをheroku上に置いて，定期実行をしています．  
実行されると，tenki.jpのサイトに行き，指定した場所の降水確率を取ってきます．  
その降水確率の値がある値(ここでは30)以上だと，twitterのapiを経由してtweetします．  

## 参考にしたサイト

- Herokuでお天気Pythonの定期実行 - Qiita  
https://qiita.com/seigo-pon/items/ca9951dac0b7fa29cce0  
- Heroku SchedulerでPythonを定期実行する - Qiita  
https://qiita.com/nsuhara/items/fac20adb6b0a122a3709
