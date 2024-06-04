import os

AIM_ENABLE_TRACKING_THREAD = '__AIM_ENABLE_TRACKING_THREAD__'
AIM_REPO_NAME = '__AIM_REPO_NAME__'
AIM_RUN_INDEXING_TIMEOUT = '__AIM_RUN_INDEXING_TIMEOUT_SECONDS__'


def get_aim_repo_name():
    return os.environ.get(AIM_REPO_NAME) or '.aim'
