from substrateinterface import Keypair

from bittensor import wallet
from bittensor.commands.transfer import TransferCommand
from bittensor.subtensor import subtensor

from ...utils import setup_wallet


# Example test using the local_chain fixture
def test_transfer(local_chain: subtensor):
    (keypair, exec_command) = setup_wallet("//Alice")
    acc_before = local_chain.get_balance(keypair.ss58_address)
    exec_command(
        TransferCommand,
        [
            "wallet",
            "transfer",
            "--amount",
            "2",
            "--dest",
            "5GpzQgpiAKHMWNSH3RN4GLf96GVTDct9QxYEFAY7LWcVzTbx",
        ],
    )
    acc_after = local_chain.get_balance(keypair.ss58_address)

    expected_transfer = 2_000_000_000
    tolerance = 200_000  # Tx fee tolerance

    actual_difference = acc_before - acc_after
    assert (
        expected_transfer <= actual_difference <= expected_transfer + tolerance
    ), f"Expected transfer with tolerance: {expected_transfer} <= {actual_difference} <= {expected_transfer + tolerance}"
