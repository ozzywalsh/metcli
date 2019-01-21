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
    panel_template = '{title} - {date}\n{text}'
    title, text, date = panel.values()
    wrapped_text = '\n'.join(textwrap.wrap(text, width=80))
    text = panel_template.format(title=colored(title, 'red'),
                                 date=colored(date, 'green'),
                                 text=wrapped_text
                                 )

    return text.strip()


def format_national(national):
    panel_names = [
        'today',
        'tonight',
        'tomorrow',
    ]

    forecast_panels = national['forecastText']['forecastPanels']

    panel_texts = []

    for panel_name in panel_names:
        panel = forecast_panels.get(panel_name)
        if panel:
            panel_texts.append(format_panel(panel))

    return '\n\n'.join(panel_texts)


def run():
    national = get_national()
    print(format_national(national))
