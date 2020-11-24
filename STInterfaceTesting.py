class STInterface:
    """
    This is an interface for making a dummy class.
    """

    def getJobDetails(self, jobname: str, num_jobs: int, job_duration: int) -> dict:
        pass

class GUIStub(STInterface):
    """
    This class implements the STInterface to test the Stress Testing Subsystem.
    This S
    """
    
    def __init__(self):
        self.jobname = 'Tapan'
        self.num_jobs = 10
        self.job_duration = 1

    def getJobDetails(self):
        details = {'jobname':self.jobname, 'num_jobs':self.num_jobs,'job_duration':self.job_duration}
        return details




