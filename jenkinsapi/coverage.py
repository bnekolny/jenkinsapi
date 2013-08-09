from jenkinsapi.jenkinsbase import JenkinsBase
from jenkinsapi.exceptions import NoCoverage
import json

class CoberturaCoverage(JenkinsBase):
    """
    Represents a coverage result of a completed Jenkins Job Build.
    """
    def __init__(self, url, job):
        self.job = job
        self.coverage_url = "{job_url}/{build_number}/cobertura/api/json" \
                .format(job_url=self.job.baseurl,
                        build_number=job.get_last_good_buildnumber())

        JenkinsBase.__init__( self, url )

    def __str__(self):
        return self._data['name']

    def get_jenkins_obj(self):
        return self.job.get_jenkins_obj()

    def get_overall_coverage(self):
        return self.get_coverage(2)
        cov_dict = self.get_coverage()['elements']
        
        self.overall_cov_dict = {}
        for item in cov_dict:
            self.overall_cov_dict[item['name']] = item['ratio']

        return self.overall_cov_dict

    def get_coverage(self, depth=5):
        #print self.coverage_url
        response = self.get_jenkins_obj().requester.get_url(
                "{coverage_url}?depth={depth}".format(coverage_url=self.coverage_url, 
                                                      depth=depth))

        try:
            json_response = json.loads(response.content)
        except ValueError:
            raise NoCoverage("%s does not have any coverage data" % str(self) )

        cov = json_response['results']
        return self._translate_coverage_json(cov)

    def _translate_coverage_json(self, response_json):
        """
        This method is going to turn the jenkins response json for coverage
        into something more usable
        """
        if isinstance(response_json, list):
            output_json = []
            for item in response_json:
                resp = self._translate_coverage_json(item)
                if len(resp) > 0:
                    output_json.append(resp)
            return output_json

        output_json = {}
        for key, val in response_json.items():
            if key == 'elements':
                for cov_item in val:
                    if not cov_item: continue
                    output_json[cov_item['name']] = cov_item['ratio']
            elif key == 'children':
                resp = self._translate_coverage_json(val)
                if len(resp):
                    output_json[key] = resp
            else:
                output_json[key] = val

        return output_json
