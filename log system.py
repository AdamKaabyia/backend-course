import datetime

def log_factory(include_timestamp=False, include_level=False):
    def log_message(message, level='INFO'):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") if include_timestamp else ''
        log_entry = f"[{level}] " if include_level else ''
        log_entry += f"{timestamp} " if timestamp else ''
        log_entry += message
        return log_entry

    return log_message


def log_processor_factory(logs):
    def filter_no_timestamp():
        return [log for log in logs if not any(char.isdigit() for char in log[:7])]

    def filter_by_timestamp_range(start, end):
        start_time = datetime.datetime.strptime(start, "%Y-%m-%d %H:%M:%S")
        end_time = datetime.datetime.strptime(end, "%Y-%m-%d %H:%M:%S")
        filtered_logs = []
        for log in logs:
            if '[' in log and ']' in log and ':' in log:
                try:
                    timestamp_end_idx = log.index(']') + 2
                    log_time = datetime.datetime.strptime(log[timestamp_end_idx:timestamp_end_idx+19], "%Y-%m-%d %H:%M:%S")
                    if start_time <= log_time <= end_time:
                        filtered_logs.append(log)
                except ValueError:
                    pass
        return filtered_logs

    def filter_short_messages(length=10):
        return [log for log in logs if len(log) < length]

    return {
        'filter_no_timestamp': filter_no_timestamp,
        'filter_by_timestamp_range': filter_by_timestamp_range,
        'filter_short_messages': filter_short_messages
    }


basic_log = log_factory()
timestamped_log = log_factory(include_timestamp=True)
detailed_log = log_factory(include_timestamp=True, include_level=True)


logs = [
    basic_log('A simple log message'),
    timestamped_log('A log message with timestamp'),
    detailed_log('A detailed log message', level='ERROR')
]

processor = log_processor_factory(logs)
print(processor['filter_no_timestamp']())
print(processor['filter_by_timestamp_range']("2023-01-01 00:00:00", "2024-12-31 23:59:59"))
print(processor['filter_short_messages']())
