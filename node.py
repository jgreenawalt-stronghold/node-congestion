class Node:
    node_data = [
            {"name":"BURMA   138 KV  MAHOCHYD","pnode_id": 1132293724,"tag": "PJMBurmaLMP","web_id":"F1DP2D-mFxStdkup8XJDcSGY4AIwwAAAU0NSUElQMDFcUEpNQlVSTUFMTVA"},
            {"name":"PINEY   12 KV   UNIT 1","pnode_id":50786,"tag":"PJMPineyLMP","web_id":"F1DP2D-mFxStdkup8XJDcSGY4AJAwAAAU0NSUElQMDFcUEpNUElORVlMTVA"}, 
            {"name":"HANDSOME LAKE","pnode_id":1104241,"tag":"PJMHandsomeLakeLMP","web_id":"F1DP2D-mFxStdkup8XJDcSGY4AJQwAAAU0NSUElQMDFcUEpNSEFORFNPTUVMQUtFTE1Q"},
            {"name":"ERIES   230 KV  LAKEVW","pnode_id":50776,"tag":"PJMErieSouthLMP","web_id":"F1DP2D-mFxStdkup8XJDcSGY4AJgwAAAU0NSUElQMDFcUEpNRVJJRVNPVVRITE1Q"},
            {"name":"COLVERPO13 KV   NUG GE","pnode_id": 50768,"tag":"PJMColverNUGLMP","web_id":"F1DP2D-mFxStdkup8XJDcSGY4AJwwAAAU0NSUElQMDFcUEpNQ09MVkVSTlVHTE1Q"},
            {"name":"UNIONCMP13 KV   UNIONC10","pnode_id": 1075455180,"tag":"PJMUnionCityLMP","web_id":"F1DP2D-mFxStdkup8XJDcSGY4AKAwAAAU0NSUElQMDFcUEpNVU5JT05DSVRZTE1Q"}
        ]

    def __init__(self, name, pnode_id, tag, web_id):
        self.name = name
        self.pnode_id = pnode_id
        self.tag = tag
        self.web_id = web_id
