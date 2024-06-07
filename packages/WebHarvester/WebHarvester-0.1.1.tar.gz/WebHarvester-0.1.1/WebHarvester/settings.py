# settings.py

# 爬虫数量
NUM_SPIDERS = 4

# 请求失败后的重试次数
RETRIES = 8

# URL 列表
URL_LIST = ['https://httpbin.org/get']

# 日志配置
LOG_LEVEL = 'INFO'

# 任务分发器配置
TASK_DISPATCHER_BATCH_SIZE = 5

# 请求超时时间
REQUEST_TIMEOUT = 10
