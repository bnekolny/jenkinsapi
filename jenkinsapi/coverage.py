from jenkinsapi.jenkinsbase import JenkinsBase
from jenkinsapi.exceptions import NoCoverage
import json

class CoberturaCoverage(JenkinsBase):
    """
    Represents a coverage result of a completed Jenkins Job Build.
    """
    def __init__(self, url, build):
        self.build = build
        self.coverage_url = "{build_url}/cobertura/api/json" \
                .format(build_url=self.build.baseurl)

        JenkinsBase.__init__( self, url )

    def __str__(self):
        return self._data['fullDisplayName']

    def get_jenkins_obj(self):
        return self.build.get_jenkins_obj()

    def get_overall_coverage(self):
        cov_dict = self.get_coverage()['elements']
        
        self.overall_cov_dict = {}
        for item in cov_dict:
            self.overall_cov_dict[item['name']] = item['ratio']

        return self.overall_cov_dict

    def get_coverage(self, depth=5):
        response = self.get_jenkins_obj().requester.get_url(
                "{coverage_url}?depth={depth}".format(coverage_url=self.coverage_url, 
                                                      depth=depth))

        try:
            json_response = json.loads(response.content)
        except ValueError:
            raise NoCoverage("%s does not have any coverage data" % str(self) )

        return json_response['results']
