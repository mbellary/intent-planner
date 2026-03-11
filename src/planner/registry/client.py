class CapabilityRegistryClient:

    def get_datasets(self):

        return [
            "eurusd_hourly",
            "eurusd_daily"
        ]

    def get_training_engines(self):

        return [
            "xgboost",
            "pytorch"
        ]

    def get_compute_engines(self):

        return [
            "spark",
            "ray"
        ]
