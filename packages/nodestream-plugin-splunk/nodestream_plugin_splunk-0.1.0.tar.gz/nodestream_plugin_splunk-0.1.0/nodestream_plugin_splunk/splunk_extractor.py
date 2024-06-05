from nodestream.pipeline import Extractor
import splunklib.client as client
import splunklib.results as results

class SplunkExtractor(Extractor):
    def __init__(self, host: str, port: int, username: str, password: str, search_query: str):
        self.HOST = host
        self.PORT = port
        self.USERNAME = username
        self.PASSWORD = password
        self.SEARCH_QUERY = search_query

    async def extract_records(self):
        service = client.connect(
            host=self.HOST,
            port=self.PORT, 
            username=self.USERNAME,
            password=self.PASSWORD)

        job = service.jobs.create(self.SEARCH_QUERY, **{"exec_mode": "blocking"})
        result_stream = job.results(output_mode='json')
        reader = results.JSONResultsReader(result_stream)
        for item in reader:
            yield item

