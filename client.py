from __future__ import division, print_function
import requests
from collections import defaultdict, OrderedDict

class IEC(object):
    def __init__(self, base_url):
        self.base_url = base_url

    def _paginate(self, url, params=None):
        params = params or {}
        url = self.base_url + "/" + url
        while url:
            r = requests.get(url, params=params)
            js = r.json()
            for result in js["results"]:
                yield result
            url = js["next"]

    def parties(self):
        return self._paginate("parties")

    def events(self):
        return self._paginate("events")

    def provinces(self):
        return self._paginate("provinces")

    def municipalities(self, **kwargs):
        return self._paginate("municipalities", kwargs)

    def wards(self, **kwargs):
        return self._paginate("wards", kwargs)

    def voting_districts(self, **kwargs):
        return self._paginate("voting_districts", kwargs)

    def results(self, **kwargs):
        return self._paginate("results", kwargs)

    def resultsummaries(self, **kwargs):
        return self._paginate("result_summaries", kwargs)

    def votes_by_ward(self, ward):
        return self._paginate("votes/by_ward", {"ward" : ward})

    def wardsummary(self, ward):
        counts = defaultdict(int)
        results = list(self.resultsummaries(ward=ward))
        if len(results) == 0:
            return None

        for vd in results:
            for k, v in vd.items():
                if type(v) == int:
                    counts[k] += v
        counts["voter_turnout_perc"] = 100 * counts["total_votes"] / counts["registered_voters"]
        results = self.results(ward=ward)

        parties = defaultdict(int)
        votes = self.votes_by_ward(ward).next()
        for r in votes["votes"]:
            parties[r["party"]] += r["votes"]
                
        counts["parties"] = OrderedDict(sorted(parties.items(), key=lambda x: x[1]))
        return dict(counts)

if __name__ == "__main__":
    iec = IEC("http://iec.code4sa.org")
    #print list(iec.parties())
    #print list(iec.events())
    #print list(iec.provinces())
    #print list(iec.municipalities(province="Gauteng"))
    #print list(iec.wards(province="Gauteng"))
    #print list(iec.voting_districts(ward="41602001"))
    #print list(iec.results(ward="41602001"))
    #print(list(iec.resultsummaries(ward="19100058")))
    print(iec.wardsummary(ward="19100058"))
    #for summary in iec.resultsummaries(province="Gauteng"):
    #    print summary["voting_district"], summary["voter_turnout_perc"]

