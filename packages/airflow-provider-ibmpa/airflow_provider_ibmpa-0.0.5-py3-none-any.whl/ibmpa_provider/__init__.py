__version__ = "0.0.5"

## This is needed to allow Airflow to pick up specific metadata fields it needs for certain features.
def get_provider_info():
    return {
        "package-name": "airflow-provider-ibmpa",  # Required
        "name": "IBM Planning Analytics",  # Required
        "description": "IBM Planning Analytics for Apache Airflow providers.",  # Required
        "connection-types": [
            {
                "connection-type": "ibmpa",
                "hook-class-name": "ibmpa_provider.hooks.ibmpa.IbmpaHook"
            }
        ],
        "versions": [__version__],  # Required
    }