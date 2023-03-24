def read_tasks(filename):
    """Функція, яка зчитує задачі та їх пріоритети з текстового файлу."""
    tasks = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip().split(',')
            if len(line) == 2:
                task, priority = line
                tasks.append((task, int(priority)))
            else:
                print(f"Рядок '{line}' у файлі містить неправильний формат та буде проігнорований.")
    return tasks


def create_queue(tasks):
    """Функція, яка створює чергу з задачами та їх пріоритетами."""
    queue = []
    for task, priority in tasks:
        if not queue:
            queue.append((task, priority))
        else:
            for i in range(len(queue)):
                if priority > queue[i][1]:
                    queue.insert(i, (task, priority))
                    break
            else:
                queue.append((task, priority))
    return queue


def is_empty(queue):
    """Функція, яка перевіряє, чи є черга порожньою."""
    return not bool(queue)


def print_tasks_and_queue(tasks, queue):
    """Функція, яка роздрукує вміст файлу та чергу."""
    print("Список задач та їх пріоритетів:")
    for task, priority in tasks:
        print(f"{task}: {priority}")
    print("\nЧерга задач:")
    if is_empty(queue):
        print("Черга порожня.")
    else:
        for task, priority in queue:
            print(f"{task}: {priority}")


# Зчитування задач та їх пріоритетів з файлу
tasks = read_tasks("tasks.txt")

# Створення черги задач
queue = create_queue(tasks)

# Роздрукування вмісту файлу та черги
print_tasks_and_queue(tasks, queue)
