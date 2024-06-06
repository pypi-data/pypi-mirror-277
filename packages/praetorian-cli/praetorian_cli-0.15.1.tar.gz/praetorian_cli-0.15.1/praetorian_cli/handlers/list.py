import json

import click

from praetorian_cli.handlers.chariot import chariot
from praetorian_cli.handlers.utils import cli_handler, list_options, key_set, get_data_key


@chariot.group()
@cli_handler
def list(ctx):
    """Get a list of resources from Chariot"""
    pass


list_filter = {'seeds': 'seed', 'assets': 'DNS', 'risks': 'seed', 'references': 'seed', 'attributes': 'seed',
               'jobs': 'updated', 'threats': 'source', 'files': 'name', 'accounts': 'name', 'integrations': 'name',
               'definitions': 'name'}


def create_list_command(item_type, item_filter):
    @list.command(item_type, help=f"List {item_type}")
    @list_options(item_filter)
    def command(controller, filter, offset, details, page):
        if item_type == 'accounts' or item_type == 'integrations':
            paginate(controller, f'{key_set[item_type]}', item_type, filter, offset, details, page)
        else:
            paginate(controller, f'{key_set[item_type]}{filter}', item_type, "", offset, details, page)


def handle_results(result, item_type):
    if item_type == 'integrations':
        result['data'] = [item for item in result['data'] if '@' not in item['member'] and item['member'] != 'settings']
    elif item_type == 'accounts':
        result['data'] = [item for item in result['data'] if '@' in item['member']]
    elif item_type == 'definitions':
        for hit in result.get('data', []):
            hit['key'] = hit['key'].split("definitions/")[-1]
    return result


def paginate(controller, key, item_type, filter, offset, details, page):
    page_size = 0
    while page_size < 100:
        result = my_result(controller, key, filter, json.dumps(offset))
        result = handle_results(result, item_type)
        display_list(result, details)
        if page == 'no' or not result.get('offset'):
            if 'offset' in result:
                print(f"Next offset: {result['offset']}")
            break
        if page == 'all':
            offset = result.get('offset')
        if page == 'interactive' and result.get('offset'):
            print("Press any key to view next or 'q' to quit")
            user_input = click.getchar()
            if user_input == 'q':
                break
            else:
                offset = result['offset']
        page_size += 1


def display_list(result, details):
    if details:
        print(json.dumps(result, indent=4))
    else:
        for hit in result.get('data', []):
            print(f"{hit['key']}")


def my_result(controller, key, filter, offset):
    resp = controller.my(dict(key=key, offset=offset))
    data_key = get_data_key(resp)
    result = {'data': resp.get(data_key, [])}
    if filter != "":  # filter by name or member only for accounts
        result['data'] = [item for item in resp['accounts'] if filter == item['name'] or filter == item['member']]
    if resp.get('offset'):
        result['offset'] = resp['offset']
    return result


for key, value in list_filter.items():
    create_list_command(key, value)
