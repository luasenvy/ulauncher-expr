import logging
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction

logger = logging.getLogger(__name__)

class ExprExtension(Extension):

  def __init__(self):
    logger.info('init Expr Extension')
    super(ExprExtension, self).__init__()
    self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())

class KeywordQueryEventListener(EventListener):

  def on_event(self, event, extension):
    items = []

    expression = event.get_argument()
    result = eval(expression)

    items = []
    items.append(ExtensionResultItem(icon='images/icon.png',
      name='Expr: %s = %s' % ( str(expression), str(result) ),
      description='Press \'enter\' to copy to clipboard.',
      on_enter=CopyToClipboardAction(str(result))
    ))

    return RenderResultListAction(items)

if __name__ == '__main__':
   ExprExtension().run()
