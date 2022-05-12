import requests

def fake_score_typing(score, cookie):

    header = {
        "cookie": str(cookie),
        "dnt": "1",
        "origin": "https://humanbenchmark.com",
        "referer": "https://humanbenchmark.com/tests/typing"
    }

    payload = {"testId":"typing","score":score}

    v = requests.post("https://humanbenchmark.com/api/v4/scores",headers=header,json=payload)
    return v

def fake_score_aim_trainer(score, cookie):

    header = {
        "cookie": str(cookie),
        "dnt": "1",
        "origin": "https://humanbenchmark.com",
        "referer": "https://humanbenchmark.com/tests/typing"
    }

    payload = {"testId": "aim", "score":score}

    v = requests.post("https://humanbenchmark.com/api/v4/scores",headers=header,json=payload)
    return v

def fake_score_sequence_memory(score, cookie):

    header = {
        "cookie": str(cookie),
        "dnt": "1",
        "origin": "https://humanbenchmark.com",
        "referer": "https://humanbenchmark.com/tests/typing"
    }

    payload = {"testId": "sequence", "score": score}

    v = requests.post("https://humanbenchmark.com/api/v4/scores",headers=header,json=payload)
    return v

def fake_score_number_memory(score, cookie):

    header = {
        "cookie": str(cookie),
        "dnt": "1",
        "origin": "https://humanbenchmark.com",
        "referer": "https://humanbenchmark.com/tests/typing"
    }

    payload = {"testId": "number-memory", "score": score}

    v = requests.post("https://humanbenchmark.com/api/v4/scores",headers=header,json=payload)
    return v

def fake_score_reaction_time(score, cookie):

    header = {
        "cookie": str(cookie),
        "dnt": "1",
        "origin": "https://humanbenchmark.com",
        "referer": "https://humanbenchmark.com/tests/typing"
    }

    payload = {"testId": "reactiontime", "score": score}

    v = requests.post("https://humanbenchmark.com/api/v4/scores",headers=header,json=payload)
    return v

def fake_score_chimp(score, cookie):

    header = {
        "cookie": str(cookie),
        "dnt": "1",
        "origin": "https://humanbenchmark.com",
        "referer": "https://humanbenchmark.com/tests/typing"
    }

    payload = {"testId": "chimp", "score": score}

    v = requests.post("https://humanbenchmark.com/api/v4/scores",headers=header,json=payload)
    return v

def fake_score_verbal_memory(score, cookie):

    header = {
        "cookie": str(cookie),
        "dnt": "1",
        "origin": "https://humanbenchmark.com",
        "referer": "https://humanbenchmark.com/tests/typing"
    }

    payload = {"testId": "verbal-memory", "score": score}

    v = requests.post("https://humanbenchmark.com/api/v4/scores",headers=header,json=payload)
    return v

def fake_score_visual_memory(score, cookie):

    header = {
        "cookie": str(cookie),
        "dnt": "1",
        "origin": "https://humanbenchmark.com",
        "referer": "https://humanbenchmark.com/tests/typing"
    }

    payload = {"testId": "memory", "score": score}

    v = requests.post("https://humanbenchmark.com/api/v4/scores",headers=header,json=payload)
    return v

h = fake_score_reaction_time(-69420,"Your_Cookie_Here")
print(h.status_code,"\n",h.headers,"\n",h.text)
