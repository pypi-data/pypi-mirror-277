import unittest


class IntegrateTests(unittest.TestCase):

    def test_markdown(self):
        from nomi.infra.renderers.markdown import MarkDown
        from nomi.infra.fetchers.apple import AppleNotesFetcher

        markdown = MarkDown()
        fetcher = AppleNotesFetcher(markdown)
        fetcher.start()