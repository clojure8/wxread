class Continuation:
    def __init__(self, success_callback, error_callback=None):
        self.success_callback = success_callback
        self.error_callback = error_callback

    def continue_with(self, result):
        try:
            self.success_callback(result)
        except Exception as e:
            if self.error_callback:
                self.error_callback(e)
            else:
                raise e

def async_operation(continuation):
    try:
        result = "done!"
        continuation.continue_with(result)
    except Exception as e:
        if continuation.error_callback:
            continuation.error_callback(e)

# 使用方式
def on_success(result):
    print(f"success: {result}")

def on_error(error):
    print(f"failed: {error}")

cont = Continuation(on_success, on_error)
async_operation(cont)