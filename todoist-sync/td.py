"""Code to fetch Todoist data with their Python library and SYNC API"""
from todoist.api import TodoistAPI

#TODO implement OAuth2 instead of the temporary TOKEN setup
TOKEN = open('keys/todoist-key.txt', 'r').readline().strip()

api = TodoistAPI(TOKEN)

api.sync()

def get_label_id(label_name: str) -> int:
    """Returns the ID of a label and raises an exception if not found
    :param str label_name: name of the label to query
    :return id
    """ 
    for label in api.state['labels']:
        if label['name'] == label_name:
            return label['id']
    raise Exception(f'Error: {label_name} is not the name of a Todoist label!')

def get_tasks_with_labels(labels: list) -> list:
    """
    Queries the api object for a filter query and returns all matching tasks containing all labels 
    :param list<str> labels: list of labels to search for (uses the AND operator)
    :return list<items> (aka tasks)
    """
    if type(labels) != list:
        raise Exception(f'Error: {labels} is not of type list!')

    # convert label names to label ID's
    label_ids = [get_label_id(label) for label in labels]

    def _contains_all_labels(item) -> bool:
        """Returns T/F if an item contains all label ids"""
        for label in label_ids:
            if label not in item['labels']:
                return False

        return True

    result = []

    for item in api.state['items']:
        if _contains_all_labels(item):
            result.append(item)

    return result

# TESTS
if __name__ == '__main__':
    print(api.state.keys())
    print()
    tasks = get_tasks_with_labels(['Events'])
    for task in tasks:
        print(task['content'])

#TODO implement method to update the start/end times for all tasks updated in GCal
# See https://developer.todoist.com/sync/v8/?python#update-an-item for updating 'items' (aka tasks)
#
# Possibly implement in separate *.py file
def update_task_from_gcal(task):
    pass