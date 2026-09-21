"""Building blocks for debugging tests by hand."""

from web.web_actions import WebActions


def pause_for_inspection(web: WebActions) -> None:
    web.pause()
