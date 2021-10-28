from django.db import models


# noinspection PyUnresolvedReferences
class ModelMixin:
    id = models.AutoField(primary_key=True)
    time_added = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)

    # abstract attributes:
    sync_functions = {}

    def str_to_repr(self, text):
        # noinspection PyUnresolvedReferences
        return f'{self.id}:{self._meta.object_name}({text})'

    def __repr__(self):
        return self.str_to_repr(str(self))

    @property
    def model_name(self):
        return self._meta.model.__name__

    def sync(self, verbose=False, propagate=True, sync_only=None, skip=None):
        """Method to sync the instance with all the other related database models. All the fields which are not
        explicit inputs to the create_from_data method depend on other models related to this instance and can
        be synced by this method whenever the related models get changed.
        This is a way around this database model being very poorly normalized (in favor of performance).

        Dependencies for the method calls:
            Molecule html sync should trigger State html sync
            State html sync should trigger Transition html sync
        """
        if sync_only is None and skip is None:
            attributes_to_sync = list(self.sync_functions)
        elif sync_only is not None:
            attributes_to_sync = sync_only
        elif skip is not None:
            attributes_to_sync = [attr for attr in self.sync_functions if attr not in skip]
        else:
            raise ValueError('Only one attribute of "sync_only", "skip" may be passed!')

        update_log = []

        for attr_name in attributes_to_sync:
            val_synced = self.sync_functions[attr_name](self)
            val_orig = getattr(self, attr_name)
            if val_synced != val_orig:
                setattr(self, attr_name, val_synced)
                update_log.append(f'updated {attr_name}: {val_orig} -> {val_synced}')
        self.save()

        if verbose and len(update_log):
            object_repr = repr(self)
            entry = update_log.pop(0)
            print(f'{object_repr}: {entry}')
            for entry in update_log:
                print(f'{len(object_repr) * " "}  {entry}')

        # sync propagation:
        if propagate:
            from elida.apps.molecule.models import Molecule
            from elida.apps.state.models import State
            if isinstance(self, Molecule) and 'html' in attributes_to_sync:
                for state in self.isotopologue.state_set.all():
                    state.sync(verbose=verbose, propagate=False,
                               sync_only=['el_state_html', 'vib_state_html', 'html'])
                for transition in self.isotopologue.transition_set.all():
                    transition.sync(verbose=verbose, propagate=False, sync_only=['html'])
            if isinstance(self, State) and 'html' in attributes_to_sync:
                for transition in self.transition_set.all():
                    transition.sync(verbose=verbose, propagate=propagate, sync_only=['html'])
