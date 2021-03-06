from __future__ import print_function
import requests
from client import IEC
from track import track

database = "wards_2006"
a2w_url = "http://wards.code4sa.org/?address={address}&database={database}"
iec_url = "http://iec.code4sa.org"


def vote_summary(address):
    url = a2w_url.format(address=address, database=database)
    js = requests.get(url).json()
    if "error" in js: 
        track("Vote - Address Not Found", address=address)
        return None

    ward = js[0]["ward"]
    iec = IEC(iec_url)

    summary = iec.wardsummary(ward=ward)
    if not summary:
        track("Vote - Ward Not Found", 
            address=js["address"], ward=js["ward"],
            municipality=js["municipality"], province=js["province"]
        )
        return None

    summary.update(js[0])
    track("Vote - Got results", user="anonymous", 
        province=summary["province"], municipality=summary["municipality"],
        ward=summary["ward"], address=summary["address"]
    )
    return summary

if __name__ == "__main__":
    input = raw_input("Please enter in your address: ")
    vs = vote_summary(input)
    if not vs:
        print("Could not find address")
    else:
        print(vs["address"])
        print("=" * 10)
        print("Special Votes: %d" % vs["special_votes"])
        print("Registered Voters: %d" % vs["registered_voters"])
        print("Section 24A Votes: %d" % vs["section_24a_votes"])
        print("Spoilt Votes: %d" % vs["spoilt_votes"])
        print("Voter Turnout: %d%%" % vs["voter_turnout_perc"])
        print("Total Votes: %.2f" % vs["total_votes"])

        print("Votes")
        for party, votes in sorted(vs["parties"].items(), key=lambda x: x[1]):
            print("%s: %d" % (party, votes))
        print("")

