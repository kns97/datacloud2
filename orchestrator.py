from generate_sample_data import main as task1
from receive_data_from_mqtt import main as task2
from create_notification import main as task3
from filter_notification import main as task4

def orchestrate_tasks():
    task1()
    task2()
    task3()
    task4()

if __name__ == "__main__":
    orchestrate_tasks()
