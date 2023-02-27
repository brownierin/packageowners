import src.go_mod as go_mod
from pathlib import Path


def test_run_go_mod():
    file = Path("tests/fixtures/package_files/go.mod")
    packages = go_mod.run_go_mod(file)
    expected = {
        "tests/fixtures/package_files/go.mod": {
            "github.com/armon/go-radix": "v1.0.0",
            "github.com/beorn7/perks": "v1.0.1",
            "golang.org/x/crypto": "v0.3.0",
            "golang.org/x/net": "v0.2.0",
            "golang.org/x/sys": "v0.2.0",
            "gopkg.in/yaml.v2": "v2.4.0",
            "gopkg.in/yaml.v3": "v3.0.1",
        }
    }

    assert expected == packages
