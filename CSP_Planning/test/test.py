from scheduler_repetition import RepetitionScheduler

sched = RepetitionScheduler(
    "uploads/repartition_cetteannee.xlsx",
    "uploads/disponibilites_exemple.xlsx",
    4, 3, 2, 60
)
sched.load_data()
sched.build_model()
sched.solve()
sched.export_planning("test_planning.xlsx")
sched.get_json_data()
