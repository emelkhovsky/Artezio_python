import website_alive.make_request as m_r


def check(a):
    if m_r.req(a).status_code == 200:
        return True
    return False
