from main import app
from scripts.deploy_staging import deploy


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.data == b"Deployment to Staging Successful!"


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.data == b"OK"


def test_staging_deployment(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    source_file = tmp_path / "main.py"
    source_file.write_text(
        "print('staging application')",
        encoding="utf-8",
    )

    result = deploy()

    deployed_file = tmp_path / "staging" / "main.py"

    assert result is True
    assert deployed_file.exists()
    assert deployed_file.read_text(encoding="utf-8") == (
        "print('staging application')"
    )