import services
import injector
import sims4.resources
from sims4.tuning.instance_manager import InstanceManager
from sims4.resources import Types

JAY_COMPUTER_IDS = (14845, 36369, 77507, 36370, 34680, 40340, 34682, 34684, 34678, 34679, 112485)
jay_writeautonomously_sa_instance_ids = (15870320921645811017, 18141105774357516002, )
    
@injector.inject_to(InstanceManager, 'load_data_into_class_instances')
def writeauto_add_superaffordances(original, self):
    original(self)

    if self.TYPE == Types.OBJECT:
        # First, get a tuple containing the tunings for all the super affordances...
        affordance_manager = services.affordance_manager()
        sa_list = []
        for sa_id in jay_writeautonomously_sa_instance_ids:
            key = sims4.resources.get_resource_key(sa_id, Types.INTERACTION)
            sa_tuning = affordance_manager.get(key)
            if not sa_tuning is None:
                sa_list.append(sa_tuning)
        sa_tuple = tuple(sa_list)

        # Now update the tunings for all the objects in our object list
        for obj_id in JAY_COMPUTER_IDS:
            key = sims4.resources.get_resource_key(obj_id, Types.OBJECT)
            obj_tuning = self._tuned_classes.get(key)
            if not obj_tuning is None:
                obj_tuning._super_affordances = obj_tuning._super_affordances + sa_tuple