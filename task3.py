import sys
from typing import List, Dict

def parse_log_line(line: str) -> dict:
    parts = line.strip().split(" ", 3)
    if len(parts) < 4:
        return None 
    date, time, level, message = parts
    return {"date": date, "time": time, "level": level, "message": message}


def load_logs(file_path: str) -> List[dict]:
    logs = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                log = parse_log_line(line)
                if log:
                    logs.append(log)
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено.")
        sys.exit(1)
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        sys.exit(1)
    return logs


def filter_logs_by_level(logs: List[dict], level: str) -> List[dict]:
    return list(filter(lambda log: log["level"].lower() == level.lower(), logs))


def count_logs_by_level(logs: List[dict]) -> Dict[str, int]:
    counts = {}
    for log in logs:
        level = log["level"]
        counts[level] = counts.get(level, 0) + 1
    return counts


def display_log_counts(counts: Dict[str, int]):
    print("\nРівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count}")


def main():
    if len(sys.argv) < 2:
        print("Використання: python main.py path/to/logfile.log [log_level]")
        sys.exit(1)

    file_path = sys.argv[1]
    logs = load_logs(file_path)

    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if len(sys.argv) > 2:
        level = sys.argv[2]
        filtered = filter_logs_by_level(logs, level)
        if filtered:
            print(f"\nДеталі логів для рівня '{level.upper()}':")
            for log in filtered:
                print(f"{log['date']} {log['time']} - {log['message']}")
        else:
            print(f"\nЗаписів рівня '{level.upper()}' не знайдено.")


if __name__ == "__main__":
    main()