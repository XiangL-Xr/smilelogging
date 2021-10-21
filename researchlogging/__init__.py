from researchlogging.logger import Logger
import configargparse
argparser = configargparse.ArgumentParser()
argparser.add_argument('--project_name', type=str, default="")
argparser.add_argument('--debug', action="store_true")
argparser.add_argument('--screen_print', action="store_true")
argparser.add_argument('--cache_ignore', type=str, default='')
argparser.add_argument('--note', type=str, default='')