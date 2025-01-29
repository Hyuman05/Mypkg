# 千葉の今日と明日の天気を表示
- このリポジトリはROS2のノードとして動作する「weather_chiba 」を提供します。

[![test](https://github.com/Hyuman05/Mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/Hyuman05/Mypkg/actions/workflows/test.yml)
## ノードの概念
- このパッケージはデータを取得して、千葉の今日と明日の天気をtopic名'weather_data'に送信します。
- 詳細　今日、明日の天気と最低気温と最高気温
- このデータは気象庁のデータを用いています。
```
  url ("https://www.jma.go.jp/bosai/forecast/#area_type=offices&area_code=120000")
  url ("https://www.jma.go.jp/bosai/forecast/data/forecast/120000.json")
```
## 依存関係
このパッケージを使用する際に必要です。
```
$ sudo apt install python3-pip
```
## 使用方法
以下のコマンドで実行します。
方法①
端末１情報を出す
```
$ ros2 run mypkg weather_chiba
```
端末２情報を受け取る
```
$ ros2 topic echo /weather_data
```
出力結果は以下の通り
```
data: "場所: 千葉県千葉市
【今日の天気】 天気: 晴れ　昼過ぎ　から　時々　くもり　所により　雨　で　雷を伴う, 最低気温: -°C, 最高気温: 12°C
【明日の天気】天気: 晴れ, 最低気温: 5°C, 最高気温: 10°C"
---

```
今日の最低気温がーなっているのはエラーではない

### テスト用コード
- listener.py
## 開発環境
- **OS**:Ubuntu 20.04 LTS
- **ROS2 version**:foxy
## テスト環境
- **OS**:Ubuntu 22.04 LTS
- **ROS2 version**:humble
## 著作権
- このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。
- @ 2025 hyuta sasaki
