import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from backend.scheduler_repetition import RepetitionScheduler

sched = RepetitionScheduler(
    "../backend/uploads/repartition_cetteannee.xlsx",
    "../backend/uploads/disponibilites_exemple.xlsx",
    4, 3, 2, 60,3
)
sched.load_data()
sched.build_model()
sched.solve()
sched.export_planning("test_planning.xlsx")
sched.get_json_data()
