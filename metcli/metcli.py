import textwrap
import sys
from termcolor import colored
import requests


def met_request(endpoint):
    try:
        url = requests.compat.urljoin('https://www.met.ie/api/', endpoint)
        return requests.get(url).json()
    except requests.exceptions.ConnectionError:
        print('There was a problem connecting to Met Éireann.')
        sys.exit()


def get_national():
    return met_request('weather/national')


def run():
    panel_names = [
        'today',
        'tonight',
        'tomorrow',
    ]

    panel_template = '{title} - {date}\n{text}'

    national = get_national()
    forecast_panels = national['forecastText']['forecastPanels']

    panel_texts = []

    for panel_name in panel_names:
        panel = forecast_panels.get(panel_name)
        if panel:
            title, text, date = panel.values()
            wrapped_text = '\n'.join(textwrap.wrap(text, width=80))
            text = panel_template.format(title=colored(title, 'red'),
                                         date=colored(date, 'green'),
                                         text=wrapped_text
                                         )

            panel_texts.append(text.strip())
    print('\n\n'.join(panel_texts))
