import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import requests
import json

class WeatherChibaNode(Node):
    def __init__(self):
        super().__init__('weather_chiba_node')
        self.publisher = self.create_publisher(String, 'weather_data', 10)
        self.timer = self.create_timer(10.0, self.publish_weather_data)
        self.get_logger().info("WeatherChibaNode has been started")

    def fetch_weather_data(self):
        try:
            url = "https://www.jma.go.jp/bosai/forecast/data/forecast/120000.json"
            response = requests.get(url)
            response.raise_for_status()
            weather_data = json.loads(response.text, )

            # JSON から天気情報を取得（千葉県 千葉市のデータ）
            today_weather = weather_data[0]["timeSeries"][0]["areas"][0]["weathers"][0]
            today_temp_min = weather_data[0]["timeSeries"][2]["areas"][0]["temps"][0]
            today_temp_max = weather_data[0]["timeSeries"][2]["areas"][0]["temps"][1]

            return f"【今日の天気】 天気: {today_weather}, 最低気温: {today_temp_min}°C, 最高気温: {today_temp_max}°C"
        except Exception as e:
            self.get_logger().error(f"天気データ取得中にエラーが発生しました: {e}")
            return "天気データを取得できませんでした。"

    def publish_weather_data(self):
        data = self.fetch_weather_data()
        msg = String()
        msg.data = f"場所: 千葉県千葉市\n{data}"
        self.publisher.publish(msg)
        self.get_logger().info(f"Published: {msg.data}")

def main():
    rclpy.init()
    node = WeatherChibaNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
