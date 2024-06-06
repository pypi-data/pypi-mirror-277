from .config import PigeonTransitionsConfig
from yaml import safe_load
from copy import copy


class MachineLoader:
    def __init__(self):
        self.machines = {}

    def load(self, config):
        for i in range(len(config)):
            for machine in config:
                if self.is_initialized(machine):
                    continue
                if self.can_init(machine):
                    self.init_machine(machine)
            if self.all_initialized(config):
                return self.machines[config[0].name]
        raise RecursionError("Unable to load state machine.")

    def all_initialized(self, config):
        return len(self.machines) == len(config)

    @staticmethod
    def has_children(machine):
        for state in machine.states:
            if "children" in state:
                return True
        return False

    @staticmethod
    def iter_children(machine):
        for state in machine.states:
            if "children" in state:
                yield state["children"]

    def children_initialized(self, machine):
        for child in self.iter_children(machine):
            if child not in self.machines:
                return False
        return True

    def can_init(self, machine):
        return self.children_initialized(machine)

    def is_initialized(self, machine):
        return machine.name in self.machines

    def init_machine(self, machine):
        kwargs = machine._as_dict
        del kwargs["type"]
        for state in kwargs["states"]:
            if not isinstance(state, dict):
                continue
            if "children" in state:
                state["children"] = self.machines[state["children"]]
        self.machines[machine.name] = machine.type(**kwargs)


class Loader:
    @classmethod
    def load(cls, config):
        machine = MachineLoader().load(config.machines)
        return machine

    @classmethod
    def from_string(cls, config):
        return cls.load(PigeonTransitionsConfig(**safe_load(config)))

    @classmethod
    def from_file(cls, confg_file):
        with open(confg_file) as f:
            return cls.from_string(f.read())
