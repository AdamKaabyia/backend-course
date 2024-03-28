import json

with open('companies.json', "r") as companies:
    org_chart_large = json.loads(companies.read())


def count_workers(node):
    count = 1  # Count the current node
    if "subordinates" in node:
        for sub in node["subordinates"]:
            count += count_workers(sub)  # Recursively count workers in subordinates
    return count


def count_cto_reports(node, searching_for_cto=True):
    if node["name"] == "CTO" and searching_for_cto:
        # Found the CTO, now count their reports
        return count_workers(node) - 1  # Exclude the CTO themselves
    elif "subordinates" in node:
        for sub in node["subordinates"]:
            count = count_cto_reports(sub, searching_for_cto=searching_for_cto)
            if count:  # If any subordinate tree has a count, return it
                return count
    return 0


def count_developers(node):
    count = 0
    if "developer" in node["name"].lower():
        count += 1
    if "subordinates" in node:
        for sub in node["subordinates"]:
            count += count_developers(sub)
    return count


def list_departments(node, departments=None):
    if departments is None:
        departments = set()
    if "subordinates" in node:
        departments.add(node["name"])
        for sub in node["subordinates"]:
            list_departments(sub, departments)
    return departments


# Perform analysis
total_workers = count_workers(org_chart_large)
cto_reports = count_cto_reports(org_chart_large, searching_for_cto=True)
developer_count = count_developers(org_chart_large)
departments = list_departments(org_chart_large)

print(f"Total Workers: {total_workers}")
print(f"CTO Reports: {cto_reports}")
print(f"Developer Count: {developer_count}")
print(f"Departments: {len(departments)}, {sorted(list(departments))}")
