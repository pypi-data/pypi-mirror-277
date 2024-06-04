# pylint: skip-file
# ruff: noqa
from opentaskpy.taskhandlers import transfer

from opentaskpy.variablecaching.aws import vc_ssm
from tests.fixtures.localstack import *  # noqa: F403

SHAREPOINT_HOST = "365devalltlab.sharepoint.com"
SHAREPOINT_SITE = "AM_Automation_LZ2"
CLIENT_ID = "d74f6327-4605-4d99-9771-be39246fc03e"
TENANT_ID = "eef422e8-c102-470c-aa74-e842a504f42f"

sharepoint_protocol_definition = {
    "name": "opentaskpy.addons.o365.remotehandlers.sharepoint.SharepointTransfer",
    "refreshToken": "",
    "clientId": CLIENT_ID,
    "tenantId": TENANT_ID,
}

sharepoint_task_definition = {
    "type": "transfer",
    "source": {
        "siteHostname": None,
        "siteName": None,
        "directory": "src",
        "fileRegex": ".*\\.txt",
        "protocol": sharepoint_protocol_definition,
        "fileWatch": {
            "timeout": 2,
        },
    },
    "cacheableVariables": [
        {
            "variableName": "source.protocol.refreshToken",
            "cachingPlugin": "file",
            "cacheArgs": {
                "file": "refresh_token.txt",
            },
        }
    ],
}


def test_dummy_transfer(ssm_client):

    # Load variables from the environment

    refresh_token = "0.Aa8A6CL07gLBDEeqdOhCpQT0LydjT9cFRplNl3G-OSRvwD6vAJo.AgABAwEAAADnfolhJpSnRYB1SVj-Hgd8AgDs_wUA9P_C-DlLzGUIXVLFWV_Kmizg37n3znf52b82r7h3-tAwCY8qbxfkQ-fF1NTjG-C0rw1Dw-2zttiOhw4m8VIXjtIjPmJaJWSvb8E21yh3ltUAYvACD9Z5j3IZt7bnVJiih7zwH4su5Z118QL5Pcje5yiyujxjO4nu2jZ4diKRHr_HCwrDBvTDWy51ErbOZ33hPTNGvkVBkr5yvCRc0sw3GlAHynaxJqgcblZOezDGC4oETBGQPPYs81CZCjGS2zP7f0wWQ21_CErayioI-LqWwjLISzKrC07gDLdtFKz6SDZ2q8YMfN97lpiu3xNA341C1CZfdIbLKo3EB9FrC6lF-vdBc95-tIgq8JOhKoZr8E2oCSIjU8nKfO70IeUgAhkK2r63Uw8q7KupPvlUtBKak8Uy9auxTOzRGk7bDEiOaJ4mRvm6Dv8S-_qGqUWVvl0bLd59XKsLikn2qTxg78WmuyYEzGAXCarzlczkowd6vYvkd6YzFgEBBREyfVtN5HY6Gj0dPFDj_IuEVozZWQLMBZ6bESW5e_ckwHH7t2sSYZVbSVwzXN6n6lzE2UCGTL-bBHgjxLpbnnpbGCW9ndlqZA8xuLR-BY3J3I6210jTxWsP9PcJvWhL2H8ne_EfWz2UQpZI03JxGTO54ORUsSl9GkMrg_axTzXkm5iZxJR4H-fYCQIQGLw7-m58ksAyRKfUvpx5uEaTCF6la_IDQFUsgEGnMShoYVNhHupFcU-Hb116K9J-1hBugYeMEuGIBV6G3kxuhn3A11ynDRIOOwwUPTPGS2KoIN-OqHlqhnoSP99kCZ9VtUxmgP1ex1p2kQvkZ--b_mg"

    # Store the refresh token in SSM
    ssm_client.put_parameter(
        Name="refresh_token",
        Value="INVALID",
        Type="SecureString",
        Overwrite=True,
    )

    sharepoint_protocol_definition["refreshToken"] = refresh_token

    transfer_obj = transfer.Transfer(
        None, "sharepoint_upload_with_ssm_token", sharepoint_task_definition
    )

    transfer_obj.run()

    # Check the parameter store value now exists and contains a random number
    param = ssm_client.get_parameter(Name="refresh_token", WithDecryption=True)
    assert param["Parameter"]["Value"] != refresh_token
    assert param["Parameter"]["Value"] != ""
