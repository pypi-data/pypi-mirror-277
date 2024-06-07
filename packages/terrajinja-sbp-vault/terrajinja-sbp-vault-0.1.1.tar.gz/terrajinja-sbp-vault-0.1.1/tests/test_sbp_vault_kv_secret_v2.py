import random

import pytest
from cdktf import Testing

from src.terrajinja.sbp.vault.kv_secret_v2 import SbpVaultKvSecretV2
from .helper import stack, has_resource, has_resource_path_value, has_resource_path_value_not_contain


class TestSbpVault:
    def test_json_formatting(self, stack):
        SbpVaultKvSecretV2(
            scope=stack,
            ns="sbp_vault_secret_json",
            data={'my_secret': 'secret'},
            mount='mount',
            name='name'
        )

        synthesized = Testing.synth(stack)

        has_resource(synthesized, "vault_kv_secret_v2")
        # has_resource_path_value(synthesized, "vault_kv_secret_v2", "sbp_vault_secret_json", "data_json",
        #                         r'${jsonencode({"my_secret" = replace("secret", "\n", "\\n")})}')
        has_resource_path_value(synthesized, "vault_kv_secret_v2", "sbp_vault_secret_json", "data_json",
                                r'${jsonencode({"my_secret" = "secret"})}')

    def test_random_password(self, stack):
        random.seed(0)
        SbpVaultKvSecretV2(
            scope=stack,
            ns="sbp_vault_random_secret",
            data={'my_secret': 'random'},
            mount='mount',
            name='name'
        )

        synthesized = Testing.synth(stack)

        has_resource(synthesized, "vault_kv_secret_v2")
        has_resource_path_value_not_contain(synthesized, "vault_kv_secret_v2", "sbp_vault_random_secret", "data_json",
                                            'random')


if __name__ == "__main__":
    pytest.main()
