from __future__ import print_function
import requests
from client import IEC

a2w_url = "http://wards.code4sa.org/?address=%s"
iec_url  = "http://iec.code4sa.org"


def vote_summary(address):
    js = requests.get(a2w_url % address).json()
    ward = js["ward"]
    iec = IEC(iec_url)

    summary = iec.wardsummary(ward=ward)
    summary["address"] = js["address"]
    return summary

if __name__ == "__main__":
    input = raw_input("Please enter in your address: ")
    vs = vote_summary(input)

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

