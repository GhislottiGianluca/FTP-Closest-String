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
            return "not found"

    for index, ss in enumerate(string_set):
        if hamming_distance(ss, si) <= d and index == len(string_set) - 1:
            return si
        elif hamming_distance(ss, si) <= d:
            continue
        else:
            break

    ssi = found_i(string_set, si, d)

    if ssi == "not found":
        return "not found"

    p = []
    pi = []

    # Instantiating p, ssi vs si
    for k in range(0, len(ssi)):
        if si[k] != ssi[k]:
            p.append(k)

    # Instantiating pi (pi subset of p, size: d+1)
    for k in range(0, d + 1):
        pi.append(p[k])

    # Recursive cycle
    for k in pi:
        s_new = list(si)
        s_new[k] = ssi[k]
        sr = FTP_closest_string(string_set, d, ''.join(s_new), d1 - 1)
        if sr != "not found":
            return sr

    return "not found"


# ---------------------------- Flask application to test the algorithm --------------------------------------

app = Flask(__name__)


@app.route('/FTP-Closest-String', methods=['POST'])
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
