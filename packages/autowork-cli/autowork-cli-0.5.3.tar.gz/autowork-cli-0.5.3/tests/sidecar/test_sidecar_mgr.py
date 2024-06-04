from multiprocessing import Process
from time import sleep

from autowork_cli.sidecar.sidecar_mgr import SidecarManager


def test_start():
    mgr = SidecarManager()
    Process(target=mgr.start).start()
    sleep(1)
    status = mgr.status()
    assert status["pid"] is not None

    mgr.stop()
    sleep(1)
    status = mgr.status()
    assert status["pid"] is None
