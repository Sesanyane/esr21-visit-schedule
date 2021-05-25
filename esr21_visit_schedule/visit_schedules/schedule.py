from dateutil.relativedelta import relativedelta
from edc_visit_schedule import Schedule, Visit as BaseVisit

# from .crfs import crf
# from .requisitions import requisitions


class Visit(BaseVisit):

    def __init__(self, crfs_unscheduled=None, requisitions_unscheduled=None,
                 crfs_prn=None, requisitions_prn=None,
                 allow_unscheduled=None, **kwargs):
        super().__init__(
            allow_unscheduled=True if allow_unscheduled is None else allow_unscheduled,
            crfs_unscheduled=crfs_unscheduled,
            requisitions_unscheduled=requisitions_unscheduled,
            crfs_prn=crfs_prn,
            requisitions_prn=requisitions_prn,
            **kwargs)


# schedule for new participants
esr21_enrollment_schedule = Schedule(
    name='ESR21_enrollment_schedule',
    verbose_name='ESR21 Enrollment Schedule',
    onschedule_model='esr21_subject.onschedule',
    offschedule_model='esr21_prn.subjectoffstudy',
    consent_model='esr21_subject.subjectconsent',
    appointment_model='edc_appointment.appointment')

visit0 = Visit(
    code='1000',
    title='Enrollment Visit',
    timepoint=0,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=None,
    crfs=None,
    facility_name='5-day clinic')

esr21_enrollment_schedule.add_visit(visit=visit0)

esr21_fu_schedule = Schedule(
    name='ESR21_fu_schedule',
    verbose_name='ESR21 Follow Up Schedule',
    onschedule_model='esr21_subject.onschedule',
    offschedule_model='esr21_prn.subjectoffstudy',
    consent_model='esr21_subject.subjectconsent',
    appointment_model='edc_appointment.appointment')

visit1 = Visit(
    code='2000',
    title='Week 1 visit',
    timepoint=2,
    rbase=relativedelta(weeks=1),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=None,
    crfs=None,
    facility_name='5-day clinic')

visit2 = Visit(
    code='3000',
    title='Week 4 visit',
    timepoint=3,
    rbase=relativedelta(weeks=4),
    rlower=relativedelta(days=3),
    rupper=relativedelta(days=3),
    requisitions=None,
    crfs=None,
    facility_name='5-day clinic')

visit3 = Visit(
    code='4000',
    title='Week 10 visit',
    timepoint=4,
    rbase=relativedelta(weeks=10),
    rlower=relativedelta(days=14),
    rupper=relativedelta(days=14),
    requisitions=None,
    crfs=None,
    facility_name='5-day clinic')

visit4 = Visit(
    code='5000',
    title='Week 11 visit',
    timepoint=5,
    rbase=relativedelta(weeks=11),
    rlower=relativedelta(days=14),
    rupper=relativedelta(days=14),
    requisitions=None,
    crfs=None,
    facility_name='5-day clinic')

visit5 = Visit(
    code='6000',
    title='Week 14 visit',
    timepoint=6,
    rbase=relativedelta(weeks=14),
    rlower=relativedelta(days=14),
    rupper=relativedelta(days=14),
    requisitions=None,
    crfs=None,
    facility_name='5-day clinic')

visit6 = Visit(
    code='6000',
    title='Week 14 visit',
    timepoint=7,
    rbase=relativedelta(weeks=26),
    rlower=relativedelta(days=3),
    rupper=relativedelta(days=3),
    requisitions=None,
    crfs=None,
    facility_name='5-day clinic')

visit7 = Visit(
    code='6000',
    title='Month 6 visit',
    timepoint=8,
    rbase=relativedelta(weeks=39),
    rlower=relativedelta(days=3),
    rupper=relativedelta(days=3),
    requisitions=None,
    crfs=None,
    facility_name='5-day clinic')

visit8 = Visit(
    code='6000',
    title='Month 12 visit',
    timepoint=9,
    rbase=relativedelta(weeks=52),
    rlower=relativedelta(days=3),
    rupper=relativedelta(days=3),
    requisitions=None,
    crfs=None,
    facility_name='5-day clinic')

esr21_fu_schedule.add_visit(visit=visit1)
esr21_fu_schedule.add_visit(visit=visit2)
esr21_fu_schedule.add_visit(visit=visit3)
esr21_fu_schedule.add_visit(visit=visit4)
esr21_fu_schedule.add_visit(visit=visit5)
esr21_fu_schedule.add_visit(visit=visit6)
esr21_fu_schedule.add_visit(visit=visit7)
esr21_fu_schedule.add_visit(visit=visit8)
