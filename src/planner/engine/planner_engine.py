from planner.engine.capability_resolver import CapabilityResolver
from planner.engine.constraint_solver import ConstraintSolver
from planner.engine.plan_generator import PlanGenerator
from planner.engine.plan_validator import PlanValidator
from planner.intent.completion import IntentCompletion
from planner.intent.normalizer import IntentNormalizer


class PlannerEngine:

    def __init__(self):

        self.normalizer = IntentNormalizer()
        self.completion = IntentCompletion()
        self.capability_resolver = CapabilityResolver()
        self.constraint_solver = ConstraintSolver()
        self.generator = PlanGenerator()
        self.validator = PlanValidator()

    def plan(self, intent):

        intent = self.normalizer.normalize(intent)

        intent = self.completion.complete(intent)

        capabilities = self.capability_resolver.resolve(intent)

        constrained_intent = self.constraint_solver.apply(intent, capabilities)

        plan = self.generator.generate(constrained_intent, capabilities)

        self.validator.validate(plan)

        return plan
