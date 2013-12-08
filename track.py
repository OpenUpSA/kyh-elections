import mixpanel
mp = mixpanel.Mixpanel("9a4e6815ec7412d57cd0bbe18f7dcb58")

def track(action, user="anonymous", **kwargs):
    mp.track(user, action, kwargs)
