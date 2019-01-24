# -*- coding: utf-8 -*-
import textwrap
import sys
from termcolor import colored
import requests


def met_request(endpoint):
    try:
        url = requests.compat.urljoin('https://www.met.ie/api/', endpoint)
        return requests.get(url).json()
    except requests.exceptions.ConnectionError:
        sys.exit('There was a problem connecting to Met Éireann.')


def get_national():
    return met_request('weather/national')


def format_panel(panel):
    title, text, date = panel.values()

    title = colored(title, 'red').strip()
    date = colored(date, 'green') if date else ''
    text = '\n'.join(textwrap.wrap(text, width=80)).strip()

    return f'{title}{" - " if len(date) > 0 else ""}{date}\n{text}'


def format_national(national):
    panel_names = [
        'today',
        'tonight',
        'tomorrow',
        'outlook'
    ]

    forecast_panels = national['forecastText']['forecastPanels']

    panel_texts = []

    for panel_name in panel_names:
        panel = forecast_panels.get(panel_name)
        if panel:
            panel_texts.append(format_panel(panel))

    return '\n\n'.join(panel_texts)


def run():
    # call the '/weather/national' endpoint and return json
    national = get_national()
    # print formatted result
    print(format_national(national))
