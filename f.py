class Future:
    def __init__(self):
        self.callbacks = []
        self.error_callbacks = []
        self.result = None
        self.error = None
        self.completed = False

    def then(self, callback):
        if self.completed and not self.error:
            callback(self.result)
        else:
            self.callbacks.append(callback)
        return self

    def catch(self, error_callback):
        if self.completed and self.error:
            error_callback(self.error)
        else:
            self.error_callbacks.append(error_callback)
        return self

    def set_result(self, result):
        self.result = result
        self.completed = True
        for callback in self.callbacks:
            callback(result)

    def set_error(self, error):
        self.error = error
        self.completed = True
        for error_callback in self.error_callbacks:
            error_callback(error)

def async_operation():
    future = Future()
    try:
        # 模拟异步操作
        result = "Done!"
        future.set_result(result)
    except Exception as e:
        future.set_error(e)
    return future

# 使用方式
async_operation()\
    .then(lambda result: print(f"Step1: {result}"))\
    .then(lambda result: print("Step2"))\
    .catch(lambda error: print(f"Error: {error}"))