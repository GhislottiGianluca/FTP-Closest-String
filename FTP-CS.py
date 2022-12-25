from typing import List
from flask import Flask, request


# Hamming Distance Function
def hamming_distance(s1, s2):

    result = 0
    for i in range(0, len(s1)):
        if s1[i] != s2[i]:
            result += 1

    return result


def found_i(string_set, s, d):
    for ss in string_set:
        if d < hamming_distance(ss, s) <= 2 * d:
            return ss

    return "not found"


# FTP algorithm for closest string (recursive approach)
def FTP_closest_string(string_set, d, si, d1):

    if d1 < 0:
        return "not found"

    for ss in string_set:
        if hamming_distance(ss, si) > d + d1:
            print(hamming_distance(ss, si))
            return "not found"

    for index, ss in enumerate(string_set):
        if hamming_distance(ss, si) <= d and index == len(string_set) - 1:
            print("primo ciclo")
            return si
        elif hamming_distance(ss, si) <= d:
            print("secondo ciclo")
            continue
        else:
            print("terzo ciclo")
            break

    ssi = found_i(string_set, si, d)
    print("this is ssi")
    print(ssi)

    if ssi == "not found":
        print("sii not found")
        return "not found"

    p = []
    pi = []

    # Instantiating p, ssi vs si
    for k in range(0, len(ssi)):
        if si[k] != ssi[k]:
            p.append(k)
    print("This is P")
    print(p)

    # Instantiating pi
    for k in range(0, d+1):
        pi.append(p[k])

    print("This is pi")
    print(pi)

    for k in pi:
        s_new = list(si)
        s_new[k] = ssi[k]
        sr = FTP_closest_string(string_set, d, ''.join(s_new), d1 - 1)
        if sr != "not found":
            return sr

    return "not found"


# ---------------------------------------------------------------------------------------------------
app = Flask(__name__)


@app.route('/prova', methods=['POST'])
def prova():

    string_set, d, s = request.json["string_set"], request.json["d"], request.json["first_string"]

    # string_set string length control
    for ss in string_set:
        if len(ss) != len(string_set[0]):
            return {"Result": "Different length in the string set"}

    # checking first_string existence in the string_set
    if s not in string_set:
        return {"Result": "first_string is not contained in the string_set"}

    return {"Result": FTP_closest_string(string_set, d, s, d)}


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

# ---------------------------------------------------------------------------------------------------
