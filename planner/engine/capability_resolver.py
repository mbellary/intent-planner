from planner.registry.client import CapabilityRegistryClient


class CapabilityResolver:

    def __init__(self):
        self.registry = CapabilityRegistryClient()

    def resolve(self, intent):

        datasets = self.registry.get_datasets()

        engines = self.registry.get_training_engines()

        compute = self.registry.get_compute_engines()

        return {
            "datasets": datasets,
            "training_engines": engines,
            "compute": compute
        }
