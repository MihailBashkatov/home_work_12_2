from utils.dicts import get_val


def test_get_val():
    assert get_val({"vcs" : "mercurial"}, "vcs") == "mercurial"
    assert get_val({"vcs": "mercurial"}, "something") == "git"
    assert get_val({}, "vcs") == "git"
    assert get_val({"vcs": "mercurial"}, "something", "python") == "python"
    assert get_val({}, "vcs", "python") == "python"