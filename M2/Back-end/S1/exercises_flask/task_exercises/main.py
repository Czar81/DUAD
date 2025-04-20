from api.task_api import start

if __name__ == "__main__":
    try:
        start()
    except Exception as error:
        print(f"An unexpected error occured: {error}")