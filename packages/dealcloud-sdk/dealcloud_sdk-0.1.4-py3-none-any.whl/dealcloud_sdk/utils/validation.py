from dealcloud_sdk.constants.auth import AVAILABLE_SCOPES


def validate_scope(scope: tuple[str]):
    """Check the assigned scope for DealCloudBase and validate all options are acceptable"""
    for s in scope:
        if s not in AVAILABLE_SCOPES:
            raise TypeError(f"s: {s} must be one of {AVAILABLE_SCOPES}")
