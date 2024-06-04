import pytest
import pandas as pd
from collections import defaultdict
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import mcap_bag_parser  # noqa: E402


SCRIPT_DIR = os.path.realpath(os.path.dirname(__file__))


def test_always_passes():
    assert True


@pytest.fixture
def parser():
    return mcap_bag_parser.BagFileParser(os.path.join(SCRIPT_DIR, 'bagfile', 'bagfile_0.mcap'))


def test_read_messages():
    num_msgs = defaultdict(lambda: 0)
    for topic, msg, timestamp in mcap_bag_parser.read_messages(
            os.path.join(SCRIPT_DIR, 'bagfile', 'bagfile_0.mcap')):
        num_msgs[topic] = num_msgs[topic] + 1
        # if topic in '/device/status':
        #     print(f"{topic} [{timestamp}]: '{msg}'")

    print(f'Found {num_msgs}')
    assert num_msgs['/rosout'] == 166
    assert num_msgs['/parameter_events'] == 9
    assert num_msgs['/robot/joint_command'] == 3998
    assert num_msgs['/device/estimated_pose'] == 3998
    assert num_msgs['/device/status'] == 3999
    assert num_msgs['/device/state'] == 3999
    assert num_msgs['/device/command'] == 6


def test_read_messages_through_class(parser):
    num_msgs = defaultdict(lambda: 0)
    for topic, msg, timestamp in parser.read_messages():
        num_msgs[topic] = num_msgs[topic] + 1
        # if topic in '/device/status':
        #     print(f"{topic} [{timestamp}]: '{msg}'")

    print(f'Found {num_msgs}')
    assert num_msgs['/rosout'] == 166
    assert num_msgs['/parameter_events'] == 9
    assert num_msgs['/robot/joint_command'] == 3998
    assert num_msgs['/device/estimated_pose'] == 3998
    assert num_msgs['/device/status'] == 3999
    assert num_msgs['/device/state'] == 3999
    assert num_msgs['/device/command'] == 6


def test_topic_to_dataframe(parser):
    df = parser.topic_to_dataframe(topic='/device/command')
    print(f'\n/device/command = \n{df}')
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 6
    assert list(df.columns) == ['arg', 'event']

    df = parser.topic_to_dataframe(topic='/device/status')
    print(f'\n/device/status = \n{df}')
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 3999
    assert 'active_driving_view' in df.columns
    assert 'state' in df.columns

    df = parser.topic_to_dataframe(topic='/robot/joint_command')
    print(f'\n/robot/joint_command = \n{df}')
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 3998
    print(df.columns)
    assert 'enable.C1_E' in df.columns
    assert 'position.C3_ROLL' in df.columns

    df = parser.topic_to_dataframe(topic='/device/estimated_pose')
    print(f'\n/device/estimated_pose = \n{df}')
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 3998
    assert 'section.DISTAL.insertion' in df.columns
    assert 'section.PROXIMAL.roll' in df.columns


def test_to_dataframe(parser):
    df = parser.to_dataframe(topics=['/device/command', '/device/status', '/robot/joint_command'])
    print(f'\ncombined dataframe = \n{df}')
    assert '/device/command.event' in df.columns
    assert '/device/status.state' in df.columns
    assert '/robot/joint_command.enable.C1_E' in df.columns


def test_topics(parser):
    topics = parser.topics
    print(topics)
    assert '/rosout' in topics
    assert '/parameter_events' in topics
    assert '/robot/joint_command' in topics
    assert '/device/estimated_pose' in topics
    assert '/device/status' in topics
    assert '/device/state' in topics
    assert '/device/estimated_pose' in topics
    assert '/device/command' in topics


def test_message_counts(parser):
    message_counts = parser.message_counts
    print(message_counts)
    assert message_counts['/device/command'] == 6
    assert message_counts['/device/estimated_pose'] == 3998
    assert message_counts['/device/status'] == 3999
