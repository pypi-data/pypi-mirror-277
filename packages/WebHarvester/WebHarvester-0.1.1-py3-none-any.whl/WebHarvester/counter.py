class Counter:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Counter, cls).__new__(cls, *args, **kwargs)
            cls._instance.total_tasks = 0
            cls._instance.completed_tasks = 0
            cls._instance.successful_tasks = 0
            cls._instance.failed_tasks = 0
            cls._instance.result_tasks = 0
        return cls._instance

    async def increment_total(self):
        self.total_tasks += 1

    async def increment_successful(self):
        self.successful_tasks += 1

    async def increment_failed(self):
        self.failed_tasks += 1

    async def increment_result(self):
        self.result_tasks += 1

    def get_summary(self):
        return {
            "total_tasks": self.total_tasks,
            "completed_tasks": self.get_completed_tasks(),
            "successful_tasks": self.successful_tasks,
            "failed_tasks": self.failed_tasks,
            "result_tasks": self.failed_tasks
        }

    def get_total_tasks(self):
        return self.total_tasks

    def get_completed_tasks(self):
        return self.successful_tasks + self.failed_tasks

    def get_successful_tasks(self):
        return self.successful_tasks

    def get_failed_tasks(self):
        return self.failed_tasks

    def get_result_tasks(self):
        return self.result_tasks
