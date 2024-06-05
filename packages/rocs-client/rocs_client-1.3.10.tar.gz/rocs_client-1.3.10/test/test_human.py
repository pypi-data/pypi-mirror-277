import time
import unittest

from rocs_client import Human
from rocs_client.robot.human import ArmAction, HandAction


async def on_connected():
    print("WebSocket opened...")


async def on_message(message: str):
    print("Received message:", message)


async def on_close():
    print("WebSocket closed")


async def on_error(error: Exception):
    print("WebSocket error:", error)


class TestHuman(unittest.TestCase):
    human = Human(on_connected=on_connected, host="192.168.12.1", on_message=on_message, on_close=on_close,
                  on_error=on_error)

    def test_enable_debug_state(self):
        res = self.human.enable_debug_state(1)
        print(f'test_enable_debug_state: {res}')
        # time.sleep(2)
        # self.human.exit()

    def test_disable_debug_state(self):
        res = self.human.disable_debug_state()
        print(f'test_disable_debug_state: {res}')
        self.human.exit()

    def test_get_video_status(self):
        res: bool = self.human.camera.video_stream_status
        print(f'test_get_video_status: {res}')
        self.human.exit()

    def test_get_video_stream_url(self):
        res: str = self.human.camera.video_stream_url
        print(f'test_get_video_stream_url:  {res}')
        self.human.exit()

    def test_get_joint_limit(self):
        res = self.human.get_joint_limit()
        print(f'test_get_joint_limit: {res}')
        self.human.exit()

    def test_get_joint_states(self):
        res = self.human.get_joint_states()
        print(f'human.test_get_joint_states: {res}')
        self.human.exit()

    def test_start(self):
        res = self.human.start()
        print(f'human.test_start: {res}')
        self.human.exit()

    def test_stop(self):
        res = self.human.stop()
        print(f'human.test_stop: {res}')
        self.human.exit()

    def test_stand(self):
        res = self.human.stand()
        print(f'human.test_stand: {res}')
        self.human.exit()

    def test_move(self):
        self.human.walk(0, 0)
        time.sleep(5)
        self.human.exit()

    def test_head(self):
        self.human.head(1, 1, 0.8)
        self.human.exit()

    def test_upper_body_arm(self):
        self.human.upper_body(arm=ArmAction.HELLO)
        self.human.exit()

    def test_upper_body_arm_waving_left_right(self):
        self.human.upper_body(arm=ArmAction.WAVING_LEFT_RIGHT)
        self.human.exit()

    def test_upper_body_arm_nvidia_dance(self):
        self.human.upper_body(arm=ArmAction.NVIDIA_DANCE)
        self.human.exit()

    def test_upper_body_hand(self):
        self.human.upper_body(hand=HandAction.TREMBLE)
        self.human.exit()

    def test_start_control_svr(self):
        for chunk in self.human._control_svr_start():
            print(chunk.decode('utf-8'))

    def test_log_view_control_svr(self):
        for chunk in self.human._control_svr_log_view():
            print(chunk.decode('utf-8'))

    def test_close_control_svr(self):
        print('test_close_control_svr: ', self.human._control_svr_close())
        self.human.exit()

    def test_status_control_svr(self):
        print('test_status_control_svr: ', self.human._control_svr_status())
        self.human.exit()

    def test_waist(self):
        self.human.waist(0, 0, 0)
        time.sleep(5)
        self.human.exit()
