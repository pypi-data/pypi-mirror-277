import typing

from everai.app import App, AppManager
from everai.commands.command import ClientCommand, command_error, ListDisplayer
from argparse import _SubParsersAction
from everai.commands.app import app_detect, add_app_name_to_parser
from everai.queue import QueuedRequest
from everai.worker import Worker


class QueueCommand(ClientCommand):
    def __init__(self, args):
        self.args = args

    @staticmethod
    @app_detect(optional=True)
    def setup(parser: _SubParsersAction, app: typing.Optional[App]):
        list_parser = parser.add_parser('queue', aliases=['q'], help='List queue of app')
        add_app_name_to_parser(list_parser, app)
        ListDisplayer.add_output_to_parser(list_parser)

        list_parser.set_defaults(func=QueueCommand)

    @command_error
    def run(self):
        queues = AppManager().list_queue(app_name=self.args.app_name)
        ListDisplayer[QueuedRequest](queues).show_list(self.args.output)
